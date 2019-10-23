function addProduct(id, name, price){
    let products = [];
    if(localStorage.getItem('products')){
        products = JSON.parse(localStorage.getItem('products'));
    }
    products.push({'id' : id, 'name' : name, 'price':price});
    localStorage.setItem('products', JSON.stringify(products));
}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

// Cuando la pagina esta lista, cargada.
document.addEventListener('DOMContentLoaded',() => {
    // si tenemos datos en el carrito renderizamos.
    if(localStorage.getItem("products")){
        const products = JSON.parse(localStorage.getItem("products"));
        let total_price = 0;
        for(i = 0; i < products.length; i++){
            const div = document.createElement('div');
            div.innerHTML = `
            <div class="row">
                <div class="col-12 text-sm-center col-sm-12 text-md-left col-md-6">
                    <h4 class="product-name"><strong>${products[i].name}</strong></h4>
                </div>
                <div class="col-12 col-sm-12 text-sm-center col-md-4 text-md-right row">
                    <div class="col-3 col-sm-3 col-md-6 text-md-right" style="padding-top: 5px">
                        <h6><strong>${products[i].price}</strong></h6>
                    </div>

                    <div class="col-2 col-sm-2 col-md-2 text-right">
                        <button data-index="${i}" type="button" id="del_item" class="btn btn-outline-danger btn-xs">
                            <i class="fa fa-trash" aria-hidden="true"></i>
                        </button>
                    </div>
                </div>
            </div>
            <hr>
            `
            document.querySelector('#productos').append(div);
            total_price =  total_price + parseFloat(products[i].price);   
                  
        }
        
        document.querySelector('#total_price').innerHTML = `${total_price.toFixed(2)} $`;

    }

    // Haciendo una orden. https://www.youtube.com/watch?v=LokXCQRBRAk

    document.querySelector('#order').onclick = () => {
        
        alert('ordenando pedido...');
        const products = JSON.parse(localStorage.getItem("products"));
        let total_price = 0;
        var data = [];
        for(i = 0; i < products.length; i++){
            var object = {
                "id":products[i].id,
                "name":products[i].name,
                "price":products[i].price
            }
            data.push(object);
        }
        console.log(data)
        console.log(JSON.stringify(data));

        $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: "POST",
            url: "/my_orders",
            dataType: "json",
            data: {"data":JSON.stringify(data)},
            success:function(data) {
                alert(data.message);
            }
        });
        
    };

    // Eliminando un producto del carrito de compras

    document.querySelectorAll('#del_item').forEach(button=>{
        button.onclick = () => {
            const index = button.dataset.index;
            const products = JSON.parse(localStorage.getItem("products"));
            
            if (index > -1) {
                products.splice(index, 1);
            }

            localStorage.setItem('products', JSON.stringify(products));
            window.location.reload();
        };
    });

    // configurando boton logout
    document.querySelector('#logout').onclick = ()=> {
        localStorage.clear();
    };

    /*
    ALGO ESTA MAL!!
    // configuring login

    document.querySelector('#login').onclick = ()=>{
        const username = document.querySelector("#username").value;
        localStorage.setItem("username", username);
        alert('loginxd');
    };
    */
    
    // Configurando botones para comprar 'buy'

    document.querySelectorAll('#buy').forEach(button => {
        button.onclick = () => {
            const id = button.dataset.id;
            const name = button.dataset.name;
            const price = button.dataset.price;
            addProduct(id,name,price);
            const li = document.createElement('li');
            li.innerHTML = `${name} ${price}`;
            document.querySelector('#carrito').append(li);
            alert(`${name} ${price}`);
            return false;
        };
    });
    


    
});
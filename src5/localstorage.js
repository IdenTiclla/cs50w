guardar_localstorage();
recuperar_localstorage();

function recuperar_localstorage(){
    var nombre = localStorage.getItem("nombre");
    alert(`localstorage: ${nombre}`);
}



function guardar_localstorage(){
    var nombre = "Iden Ticlla";
    localStorage.setItem("nombre",nombre);
}

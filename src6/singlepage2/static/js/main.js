// When the document is loaded
document.addEventListener('DOMContentLoaded', () => {
    load_page('first');

    document.querySelectorAll('.nav-link').forEach(link => {
        link.onclick = ()=>{
            const page = link.dataset.page;
            load_page(page)
            return false;
        };
    });
});

window.onpopstate = e =>{
    const data = e.state;
    document.title = data.title;
    document.querySelector('#body'). innerHTML = data.text;
}

function load_page(name){
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        const response = request.responseText;
        document.querySelector('#body').innerHTML = response;

        document.title = name;
        history.pushState({'title': name, 'text': response}, name, name);
    };
    request.send();
}
//by iden xd
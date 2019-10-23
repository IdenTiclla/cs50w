document.addEventListener("DOMContentLoaded", () => {
    load_page('first');
    
    document.querySelectorAll(".nav-link").forEach(link => {
        link.onclick = () => {
            const page = link.dataset.page;
            load_page(page);
            return false;
        };
    });
});

function load_page(name){
    const request = new XMLHttpRequest();
    request.open("GET",`/${name}`);
    request.onload = () => {
        const response = request.responseText;
        document.querySelector("#body").innerHTML = response;

        document.title = name;
        history.pushState(null, name, name);
    };
    request.send();
}
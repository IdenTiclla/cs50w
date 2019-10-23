// When the document is loaded
document.addEventListener("DOMContentLoaded", () => {
    // load the first page
    load_page('first');
    // configure to load all other pages
    document.querySelectorAll('.nav-link').forEach(link => {
        link.onclick = () => {
            const page = link.dataset.page;
            load_page(page);
            return false;
        }
    });
});

function load_page(name){
    const request = new XMLHttpRequest();
    request.open("GET",`/${name}`);
    request.onload = () => {
        const response = request.responseText;
        document.querySelector("#body").innerHTML = response;
    };
    request.send();
}
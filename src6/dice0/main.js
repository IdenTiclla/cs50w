const template = Handlebars.compile("<li>Lanzaste el dado {{ value }}</li>");
// When the document is loaded
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#roll').onclick = () =>{
        const roll = Math.floor((Math.random() * 6) + 1);
        const li = template({"value":roll});
        document.querySelector('#rolls').innerHTML += li;
    };
});
// by iden 
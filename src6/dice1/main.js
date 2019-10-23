const template = Handlebars.compile("<li><img src=\"img/{{value}}.png\"></li>");

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#roll').onclick = () => {
        const roll = Math.floor((Math.random() * 6) + 1);
        const li = template({"value":roll});
        document.querySelector('#rolls').innerHTML += li;
    };
});
let counter = 1;
const quantity = 20;


document.addEventListener('DOMContentLoaded', load);

window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

function load(){
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    const request = new XMLHttpRequest();
    request.open("POST",'/posts');
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        data.forEach(add_post);
    };
    
    const data = new FormData();
    data.append('start', start);
    data.append('end', end);
    
    request.send(data);
}

function add_post(contents){
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = contents;

    const hide = document.createElement('button');
    hide.className = 'hide';
    hide.innerHTML = 'hide';

    hide.onclick = function(){
        this.parentElement.remove();
    }

    post.appendChild(hide);

    document.querySelector('#posts').append(post);

}
// by iden xdddd posts1
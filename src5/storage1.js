if (!localStorage.getItem('counter'))
    localStorage.setItem('counter', 0);

document.addEventListener('DOMContentLoaded', () => {
    setInterval(count, 1000);
});

function count(){
    var counter = localStorage.getItem('counter')
    counter++;
    localStorage.setItem('counter',counter);
    document.querySelector('#counter').innerHTML = localStorage.getItem('counter');
}

document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#button1').onclick = count;
    document.querySelector('#button2').onclick = discount;
});

var counter = 0;

function count(){
    counter += 1;
    document.querySelector('#counter').innerHTML = counter;
}

function discount(){
    counter -= 1;
    document.querySelector('#counter').innerHTML = counter;
}
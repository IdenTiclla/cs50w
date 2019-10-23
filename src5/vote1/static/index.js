document.addEventListener('DOMContentLoaded', ()=>{
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', ()=>{
        document.querySelectorAll('button').forEach(button =>{
            button.onclick = ()=>{
                const selection = button.dataset.vote;
                socket.emit('submit vote', {"selection":selection});
            };
        });
    });
    socket.on('announce vote', data=>{
        document.querySelector('#yes').innerHTML = `yes: ${data.yes}.`;
        document.querySelector('#no').innerHTML = `no: ${data.no}.`;
        document.querySelector('#maybe').innerHTML = `maybe: ${data.maybe}.`;
    });
});
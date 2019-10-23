document.addEventListener('DOMContentLoaded', () => {
    const h1 = document.querySelector('h1');
    const button = document.querySelector('button');
    h1.style.animationPlayState = 'paused';
    button.onclick = () => {
        if(h1.style.animationPlayState === 'paused')
            h1.style.animationPlayState = 'running';
        else
            h1.style.animationPlayState = 'paused';
    };
});
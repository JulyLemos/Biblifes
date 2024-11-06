for (let i = 0; i < 1000; i++) {
    let star = document.createElement('div');
    star.className = 'star';
    star.style.top = Math.random() * 100 + '%';
    star.style.left = Math.random() * 100 + '%';
    star.style.opacity = Math.random();
    star.style.animation = `twinkle ${Math.random() * 5 + 5}s linear ${Math.random() * 5}s infinite`;
    document.body.appendChild(star);
}
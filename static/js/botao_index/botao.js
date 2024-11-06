// carregar arquivo JSON 
fetch('/static/json/frases.json')
.then(response => response.json())
.then(frases => {
    // frase aleatória 
    const fraseAleatoria = frases[Math.floor(Math.random() * frases.length)];
    // inserir a frase 
    document.getElementById('frase').innerText = fraseAleatoria.frase;
    document.getElementById('autor').innerText = `— ${fraseAleatoria.autor}`;
    
    // botão aparecendo depois de 2s
    setTimeout(() => {
        document.getElementById('continuar').style.display = 'block'; 
    }, 2000);
})
.catch(error => {  //caso dê algum erro ao carregar a frase
    console.error('Erro ao carregar o arquivo JSON:', error);
    document.getElementById('frase').innerText = 'Erro ao carregar a frase.';
    document.getElementById('autor').innerText = '';
});


// redirecionar a uma outra página depois de 2 segundos ao clicar no botão
document.getElementById('continuar').addEventListener('click', () => {
document.getElementById('continuar').disabled = true; // desabilita o botão
setTimeout(() => {
    window.location.href = 'lar'; 
}, 1000);
});
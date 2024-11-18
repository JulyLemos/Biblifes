 //redirecionamento de página - mudar no sql
 document.getElementById('continuar').addEventListener('click', () => {
    document.getElementById('continuar').disabled = true; // desabilita o botão
    setTimeout(() => {
        window.location.href = 'lar'; 
    }, 2000);
});
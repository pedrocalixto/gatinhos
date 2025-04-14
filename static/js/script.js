// JavaScript para a Galeria de Gatinhos Fofos
document.addEventListener('DOMContentLoaded', function() {
    console.log('Galeria de Gatinhos Fofos carregada com sucesso!');
    
    // Adiciona uma animação simples aos cards de gatos
    const catCards = document.querySelectorAll('.cat-card');
    
    catCards.forEach((card, index) => {
        // Adiciona um pequeno atraso a cada card para um efeito escalonado
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 * index);
    });
    
    // Adiciona evento de clique aos cards de gatos para mostrar uma interação simples
    catCards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('expanded');
            
            // Se o card estiver expandido, rola para ele
            if (this.classList.contains('expanded')) {
                this.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });
    });
});

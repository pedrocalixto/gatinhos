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

    // Função para atualizar as curiosidades sobre gatos a cada 10 segundos
    function updateCatFacts() {
        const factsContainer = document.getElementById('facts-container');
        
        // Se o container não existir, não faz nada
        if (!factsContainer) return;
        
        // Faz uma requisição para a API de curiosidades
        fetch('/api/facts/random')
            .then(response => response.json())
            .then(facts => {
                // Cria o HTML para as novas curiosidades
                let newFactsHTML = '';
                facts.forEach(fact => {
                    newFactsHTML += `
                        <div class="fact" style="opacity: 0;">
                            <i class="fas ${fact.icon}"></i>
                            <p>${fact.fact}</p>
                        </div>
                    `;
                });
                
                // Aplica uma animação de fade-out nas curiosidades atuais
                const currentFacts = factsContainer.querySelectorAll('.fact');
                currentFacts.forEach(fact => {
                    fact.style.opacity = '0';
                    fact.style.transform = 'translateY(-20px)';
                });
                
                // Após a animação de fade-out, substitui as curiosidades e faz fade-in
                setTimeout(() => {
                    factsContainer.innerHTML = newFactsHTML;
                    
                    // Aplica animação de fade-in nas novas curiosidades
                    const newFacts = factsContainer.querySelectorAll('.fact');
                    newFacts.forEach((fact, index) => {
                        setTimeout(() => {
                            fact.style.opacity = '1';
                            fact.style.transform = 'translateY(0)';
                        }, 100 * index);
                    });
                }, 500);
            })
            .catch(error => {
                console.error('Erro ao buscar curiosidades:', error);
            });
    }
    
    // Atualiza as curiosidades a cada 10 segundos
    setInterval(updateCatFacts, 10000);
});

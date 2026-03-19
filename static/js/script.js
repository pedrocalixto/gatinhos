document.addEventListener('DOMContentLoaded', function () {
    initCardAnimations();
    initCardInteractions();
    initFactsRotation();
});

function initCardAnimations() {
    const cards = document.querySelectorAll('.cat-card');
    cards.forEach(function (card, index) {
        setTimeout(function () {
            card.classList.add('is-visible');
        }, 100 * index);
    });
}

function initCardInteractions() {
    const cards = document.querySelectorAll('.cat-card');
    cards.forEach(function (card) {
        card.addEventListener('click', function () {
            this.classList.toggle('expanded');
            if (this.classList.contains('expanded')) {
                this.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });
}

function initFactsRotation() {
    const container = document.getElementById('facts-container');
    if (!container) return;
    setInterval(function () { rotateFacts(container); }, 10000);
}

function rotateFacts(container) {
    fetch('/api/facts/random')
        .then(function (response) { return response.json(); })
        .then(function (facts) {
            const current = container.querySelectorAll('.fact');
            current.forEach(function (el) { el.classList.add('is-hidden'); });

            setTimeout(function () {
                container.innerHTML = facts.map(function (fact) {
                    return (
                        '<div class="fact is-hidden">' +
                        '<i class="fas ' + fact.icon + '"></i>' +
                        '<p>' + fact.fact + '</p>' +
                        '</div>'
                    );
                }).join('');

                container.querySelectorAll('.fact').forEach(function (el, index) {
                    setTimeout(function () { el.classList.remove('is-hidden'); }, 100 * index);
                });
            }, 500);
        })
        .catch(function (error) {
            console.error('Erro ao buscar curiosidades:', error);
        });
}

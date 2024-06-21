// document.addEventListener('DOMContentLoaded', function() {
//     const form = document.querySelector('form');
//     form.addEventListener('submit', function(event) {
//         const btn = document.querySelector('.btn');
//         btn.innerHTML = 'Calculating...';
//         setTimeout(() => {
//             btn.innerHTML = 'Calculate';
//         }, 1000);
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const btn = document.querySelector('.btn');
        btn.innerHTML = 'Calculating...';
        setTimeout(() => {
            btn.innerHTML = 'Calculate';
        }, 1000);
    });
});

function calculateNewPrice(result) {
    const currentPrice = parseFloat(document.getElementById('current_price').value);
    if (!isNaN(result) && !isNaN(currentPrice)) {
        const newPrice = currentPrice * (1 + result / 100);
        document.getElementById('new_price_result').innerHTML = `<h2>New Price: <span>${newPrice.toFixed(2)} $</span></h2>`;
    } else {
        document.getElementById('new_price_result').innerHTML = `<h2>Please enter a valid current price.</h2>`;
    }
}


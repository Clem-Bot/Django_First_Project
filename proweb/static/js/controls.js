// Color change buttons
document.getElementById('darkBtn').addEventListener('click', function() {
    document.body.style.color = '#333';
    document.querySelectorAll('h1, h2, h3').forEach(el => {
        el.style.color = '#333';
    });
});

document.getElementById('blueBtn').addEventListener('click', function() {
    document.body.style.color = '#2196F3';
    document.querySelectorAll('h1, h2, h3').forEach(el => {
        el.style.color = '#2196F3';
    });
});

document.getElementById('redBtn').addEventListener('click', function() {
    document.body.style.color = '#f44336';
    document.querySelectorAll('h1, h2, h3').forEach(el => {
        el.style.color = '#f44336';
    });
});

document.getElementById('greenBtn').addEventListener('click', function() {
    document.body.style.color = '#4caf50';
    document.querySelectorAll('h1, h2, h3').forEach(el => {
        el.style.color = '#4caf50';
    });
});

// Text size slider
document.getElementById('textSizeSlider').addEventListener('input', function() {
    const size = this.value + 'px';
    document.body.style.fontSize = size;
    document.getElementById('sizeValue').textContent = this.value + 'px';
});

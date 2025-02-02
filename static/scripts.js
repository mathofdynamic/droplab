function rewriteTitle() {
    const title = document.getElementById('title').value;
    const tone = document.getElementById('tone').value;
    fetch('/rewrite_title', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: title, tone: tone })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.style.opacity = 0;
        setTimeout(() => {
            resultDiv.textContent = data.rewritten_title;
            resultDiv.style.opacity = 1;
            resultDiv.classList.add('fade-in-up');
            setTimeout(() => {
                resultDiv.classList.remove('fade-in-up');
            }, 1000);
        }, 500);
    });
}

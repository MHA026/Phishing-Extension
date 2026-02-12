document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        const currentUrl = tabs[0].url;
        scanUrl(currentUrl);
    });
});

function scanUrl(url) {
    const statusElement = document.getElementById('status');
    const iconElement = document.getElementById('icon');
    const scoreElement = document.getElementById('scoreDetails');

    fetch('http://127.0.0.1:8000/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
        .then(response => response.json())
        .then(data => {
            const score = data.score;
            const verdict = data.verdict;

            let colorClass = '';
            let icon = '';

            if (verdict === 'Safe') {
                colorClass = 'safe';
                icon = '✅';
            } else if (verdict === 'Suspicious') {
                colorClass = 'suspicious';
                icon = '⚠️';
            } else {
                colorClass = 'phishing';
                icon = '⛔';
            }

            statusElement.textContent = verdict;
            statusElement.className = 'status-text ' + colorClass;

            iconElement.textContent = icon;
            iconElement.className = 'status-icon ' + colorClass;

            scoreElement.textContent = `Phishing Score: ${score}%`;
        })
        .catch(error => {
            statusElement.textContent = "Error";
            statusElement.className = 'status-text phishing';
            iconElement.textContent = '❌';
            scoreElement.textContent = "Server not reachable";
            console.error('Error:', error);
        });
}

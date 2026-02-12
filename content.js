chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Message received in content script:", request);
    if (request.action === "showWarning") {
        createWarningPopup(request.score);
    }
});

function createWarningPopup(score) {
    // Visual alarm: Red border on body
    document.body.style.border = "5px solid #e74c3c";
    document.body.style.boxSizing = "border-box";

    // Check if popup already exists
    if (document.getElementById('phishguard-shadow-host')) return;

    const host = document.createElement('div');
    host.id = 'phishguard-shadow-host';
    document.body.appendChild(host);

    const shadow = host.attachShadow({ mode: 'open' });

    const link = document.createElement('link');
    link.setAttribute('rel', 'stylesheet');
    link.setAttribute('href', chrome.runtime.getURL('styles.css'));
    shadow.appendChild(link);

    const popup = document.createElement('div');
    popup.className = 'phishguard-popup';

    popup.innerHTML = `
        <div class="phishguard-content">
            <div class="phishguard-icon">⚠️</div>
            <div class="phishguard-text">
                <strong>High Risk Detected</strong>
                <p>Phishing Score: ${score}%</p>
                <p>Proceed with Caution.</p>
            </div>
            <button class="phishguard-close">×</button>
        </div>
    `;

    shadow.appendChild(popup);

    const closeBtn = popup.querySelector('.phishguard-close');
    closeBtn.addEventListener('click', () => {
        host.remove();
    });
}

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url) {
        console.log(`Tab updated: ${tab.url}`);
        if (tab.url.startsWith('http')) {
            checkUrl(tabId, tab.url);
        }
    }
});

function checkUrl(tabId, url) {
    console.log(`Checking URL: ${url}`);
    fetch('http://127.0.0.1:8000/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
        .then(response => response.json())
        .then(data => {
            console.log(`Scan result for ${url}:`, data);
            if (data.score > 60) {
                console.log("High risk detected, sending message to content script...");

                const sendMessageWithRetry = (retries) => {
                    chrome.tabs.sendMessage(tabId, {
                        action: "showWarning",
                        score: data.score
                    }).catch(err => {
                        if (retries > 0) {
                            console.log(`Message failed, retrying... (${retries} left)`);
                            setTimeout(() => sendMessageWithRetry(retries - 1), 1000);
                        } else {
                            console.log("Error sending message after retries:", err);
                        }
                    });
                };

                sendMessageWithRetry(3); // Retry 3 times

                // Update badge
                chrome.action.setBadgeText({ text: "!", tabId: tabId });
                chrome.action.setBadgeBackgroundColor({ color: "#e74c3c", tabId: tabId });
            }
        })
        .catch(error => console.log('Error checking URL:', error));
}

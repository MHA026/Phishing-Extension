import pandas as pd
import numpy as np
import re
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Generate Synthetic Dataset
def generate_data():
    safe_urls = [
        "https://www.google.com", "https://www.youtube.com", "https://www.facebook.com",
        "https://www.amazon.com", "https://www.wikipedia.org", "https://www.reddit.com",
        "https://www.netflix.com", "https://www.linkedin.com", "https://www.microsoft.com",
        "https://www.apple.com", "https://www.instagram.com", "https://www.twitter.com",
        "https://www.twitch.tv", "https://www.stackoverflow.com", "https://www.github.com",
        "https://www.dropbox.com", "https://www.salesforce.com", "https://www.paypal.com",
        "https://www.cnn.com", "https://www.nytimes.com", "https://www.bbc.co.uk",
        "https://www.weather.com", "https://www.espn.com", "https://www.adobe.com",
        "https://www.spotify.com", "https://www.whatsapp.com", "https://www.tiktok.com",
        "https://www.zoom.us", "https://www.slack.com", "https://www.trello.com",
        "https://www.airbnb.com", "https://www.booking.com", "https://www.uber.com",
        "https://www.lyft.com", "https://www.doordash.com", "https://www.grubhub.com",
        "https://www.instacart.com", "https://www.target.com", "https://www.walmart.com",
        "https://www.bestbuy.com", "https://www.homedepot.com", "https://www.lowes.com",
        "https://www.costco.com", "https://www.ikea.com", "https://www.wayfair.com",
        "https://www.etsy.com", "https://www.ebay.com", "https://www.craigslist.org",
        "https://www.zillow.com", "https://www.realtor.com"
    ]

    phishing_urls = [
        "http://secure-bank-login-verify.example.com/login",
        "http://paypal-security-update.badsite.com/confirm",
        "http://amazon-account-suspended.phish.net/verify",
        "http://apple-id-locked.support-apple.com.bad.com",
        "http://netflix-payment-failed.update-account.net",
        "http://google-drive-share.login-verify.com",
        "http://facebook-security-alert.confirm-identity.org",
        "http://microsoft-office-update.required-action.net",
        "http://linkedin-job-offer.view-details.xyz",
        "http://twitter-verified-badge.claim-now.site",
        "http://instagram-copyright-violation.appeal-form.com",
        "http://dropbox-file-transfer.download-now.net",
        "http://salesforce-crm-login.employee-portal.org",
        "http://chase-bank-alert.verify-account.com",
        "http://wells-fargo-security.update-info.net",
        "http://bank-of-america-login.secure-access.com",
        "http://citibank-alert.confirm-details.org",
        "http://capital-one-verify.card-activation.net",
        "http://american-express-login.secure-portal.com",
        "http://irs-tax-refund.claim-status.gov.bad.com",
        "http://ups-delivery-failed.reschedule-package.net",
        "http://fedex-tracking-update.confirm-address.org",
        "http://dhl-shipping-alert.view-details.com",
        "http://usps-package-hold.release-package.net",
        "http://amazon-prime-renewal.payment-update.com",
        "http://walmart-gift-card.claim-reward.net",
        "http://target-shopper-survey.win-prize.org",
        "http://bestbuy-order-confirmation.view-receipt.com",
        "http://apple-support.icloud-login.net",
        "http://microsoft-teams-invite.join-meeting.org",
        "http://zoom-meeting-link.secure-connect.com",
        "http://slack-workspace-login.team-portal.net",
        "http://adobe-creative-cloud.update-license.org",
        "http://spotify-premium-expired.renew-now.com",
        "http://netflix-account-hold.update-payment.net",
        "http://hulu-subscription-issue.verify-card.org",
        "http://disney-plus-login.member-access.com",
        "http://coinbase-wallet-alert.verify-identity.net",
        "http://binance-security-check.confirm-withdrawal.org",
        "http://blockchain-wallet-login.secure-access.com",
        "http://192.168.1.1/login",
        "http://10.0.0.1/admin",
        "http://verify-account-now.com",
        "http://login-secure-update.net",
        "http://update-payment-info.org",
        "http://confirm-identity-required.com",
        "http://account-suspended-action.net",
        "http://security-alert-verify.org",
        "http://urgent-action-required.com",
        "http://important-notification.net"
    ]

    data = []
    for url in safe_urls:
        data.append({"url": url, "label": 0}) # 0 for Safe
    for url in phishing_urls:
        data.append({"url": url, "label": 1}) # 1 for Phishing

    return pd.DataFrame(data)

# 2. Feature Extraction
def extract_features(url):
    features = {}
    
    # URL Length
    features['url_length'] = len(url)
    
    # Count of dots, hyphens, and "@" symbols
    features['dot_count'] = url.count('.')
    features['hyphen_count'] = url.count('-')
    features['at_count'] = url.count('@')
    
    # Presence of IP address in domain (simplified check)
    # Matches standard IPv4 patterns
    ip_pattern = r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    features['has_ip'] = 1 if re.search(ip_pattern, url) else 0
    
    # Presence of keywords
    features['has_login'] = 1 if 'login' in url.lower() else 0
    features['has_verify'] = 1 if 'verify' in url.lower() else 0
    features['has_update'] = 1 if 'update' in url.lower() else 0
    
    return features

# 3. Train Model
def train_model():
    print("Generating synthetic dataset...")
    df = generate_data()
    
    print("Extracting features...")
    # Apply feature extraction to all URLs
    features_list = [extract_features(url) for url in df['url']]
    X = pd.DataFrame(features_list)
    y = df['label']
    
    print("Training Random Forest Classifier...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    print("Saving model...")
    joblib.dump(clf, 'phishing_model.pkl')
    print("Model saved as 'phishing_model.pkl'")

if __name__ == "__main__":
    train_model()

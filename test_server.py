from server import extract_features, scan_url, URLRequest
import joblib

# Test Feature Extraction
url = "http://secure-bank-login-verify.example.com/login"
features = extract_features(url)
print("Features:", features)

# Test Prediction Logic (Mocking request)
req = URLRequest(url=url)
try:
    result = scan_url(req)
    print("Scan Result:", result)
except Exception as e:
    print("Scan Error:", e)

# Test Safe URL
safe_url = "https://www.google.com"
req_safe = URLRequest(url=safe_url)
try:
    result_safe = scan_url(req_safe)
    print("Safe Scan Result:", result_safe)
except Exception as e:
    print("Safe Scan Error:", e)

# Phishing URL Detection System Walkthrough

This document guides you through setting up and running the End-to-End Phishing URL Detection System.

## Prerequisites
- Python 3.x installed
- Google Chrome browser

## Phase 1: Model Training
The model has already been trained using synthetic data.
- **Script**: `train_model.py`
- **Model File**: `phishing_model.pkl` (Generated)

If you need to retrain the model:
```bash
python train_model.py
```

## Phase 2: Start the Backend Server
The server hosts the machine learning model and provides an API for the extension.

1. Open a terminal in `d:\PhishMain`.
2. Run the server:
   ```bash
   uvicorn server:app --reload
   ```
   The server will start at `http://127.0.0.1:8000`.

## Phase 3: Install the Chrome Extension
1. Open Google Chrome.
2. Navigate to `chrome://extensions`.
3. Enable **Developer mode** in the top right corner.
4. Click **Load unpacked**.
5. Select the folder `d:\PhishMain\PhishGuard`.

## Usage
1. **Popup Scan**: Click the PhishGuard icon in the Chrome toolbar to scan the current tab.
2. **Real-time Protection**: The extension automatically scans URLs as you browse.
   - If a high-risk URL is detected (Score > 60%), a warning popup will appear in the bottom right corner.

## Testing
You can test the system with these URLs (Note: These are safe to visit as they are just strings for the model, but be careful with actual navigation if they were real):
- **Safe**: `https://www.google.com`
- **Phishing Pattern**: `http://secure-bank-login-verify.example.com/login`

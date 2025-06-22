import os
import json
import subprocess
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
GUMROAD_PRODUCT_ID = "YOUR_PRODUCT_ID_HERE"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate-license", methods=["POST"])
def validate_license():
    data = request.get_json()
    license_key = data.get("license_key")
    if not license_key:
        return jsonify({"success": False, "message": "License key is required."}), 400
    if GUMROAD_PRODUCT_ID == "YOUR_PRODUCT_ID_HERE":
        if license_key.startswith("IRON-VALID-"):
            return jsonify({
                "success": True,
                "message": "License is valid (Simulated).",
                "purchase": {"product_name": "IRONVAULT - Hybrid Tier"}
            })
        else:
            return jsonify({"success": False, "message": "License is invalid (Simulated)."}), 400
    try:
        api_response = requests.post(
            "https://api.gumroad.com/v2/licenses/verify",
            data={"product_id": GUMROAD_PRODUCT_ID, "license_key": license_key.strip()}
        )
        api_response.raise_for_status()
        response_data = api_response.json()
        if response_data.get("success"):
            return jsonify({
                "success": True,
                "message": f"License is valid for {response_data['purchase']['product_name']}.",
                "purchase": response_data.get("purchase")
            })
        else:
            return jsonify({"success": False, "message": response_data.get("message", "License is invalid.")}), 400
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return jsonify({"success": False, "message": "Could not connect to Gumroad API."}), 500

@app.route("/test-webhook", methods=["POST"])
def test_webhook():
    data = request.get_json()
    url = data.get("webhook_url")
    if not url or not url.startswith("https://discord.com/api/webhooks/"):
        return jsonify({"success": False, "message": "Invalid Discord webhook URL format."}), 400
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "embeds": [{
            "title": "✅ IRONVAULT Connection Test",
            "description": "If you can see this, your webhook is configured correctly!",
            "color": 5763719
        }]
    })
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=5)
        response.raise_for_status()
        return jsonify({"success": True, "message": "Test message sent successfully!"})
    except requests.exceptions.RequestException as e:
        print(f"Webhook Error: {e}")
        return jsonify({"success": False, "message": "Could not connect to webhook URL."}), 500

@app.route("/save-config", methods=["POST"])
def save_config():
    config_data = request.get_json()
    if not all(k in config_data for k in ["license_key", "tier", "discord_webhook"]):
        return jsonify({"success": False, "message": "Missing configuration data."}), 400
    try:
        with open("config.json", "w") as f:
            json.dump(config_data, f, indent=4)
        return jsonify({"success": True, "message": "Configuration saved to config.json."})
    except IOError as e:
        print(f"File Save Error: {e}")
        return jsonify({"success": False, "message": "Error saving configuration file."}), 500

@app.route("/start-bot", methods=["POST"])
def start_bot():
    bot_executable = "main.exe"
    if not os.path.exists(bot_executable):
        return jsonify({"success": False, "message": f"{bot_executable} not found in root directory."}), 404
    try:
        subprocess.Popen([bot_executable])
        return jsonify({"success": True, "message": "Bot process has been started."})
    except Exception as e:
        print(f"Subprocess Error: {e}")
        return jsonify({"success": False, "message": "Failed to start the bot process."}), 500

if __name__ == "__main__":
    print("--- IRONVAULT Config Dashboard ---")
    print("Navigate to http://127.0.0.1:5000 in your web browser.")
    app.run(host="0.0.0.0", port=5000, debug=True)

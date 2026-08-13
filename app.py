from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_NAME = os.getenv("APP_NAME", "HealthWatch")
SIMULATE_FAILURE = os.getenv("SIMULATE_FAILURE", "false").lower() == "true"
SIMULATE_DELAY = float(os.getenv("SIMULATE_DELAY", "0"))

@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "message": "HealthWatch application is running",
        "status": "UP"
    })

@app.route("/health")
def health():
    if SIMULATE_FAILURE:
        return jsonify({
            "status": "DOWN",
            "version": APP_VERSION
        }), 503

    if SIMULATE_DELAY > 0:
        time.sleep(SIMULATE_DELAY)

    return jsonify({
        "status": "UP",
        "version": APP_VERSION
    }), 200

@app.route("/version")
def version():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "unknown")
ENVIRONMENT = os.getenv("ENVIRONMENT", "unknown")
HEALTH_STATUS = os.getenv("HEALTH_STATUS", "healthy")


@app.get("/")
def home():
    return jsonify(
        application="harness-seeker-demo",
        version=APP_VERSION,
        environment=ENVIRONMENT,
        status="running"
    )


@app.get("/health")
def health():
    if HEALTH_STATUS == "unhealthy":
        return jsonify(status="unhealthy"), 500

    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

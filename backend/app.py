from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_NAME = "teamboard-backend"
SERVICE_VERSION = "1.0.0"


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": SERVICE_NAME})


@app.route("/api/info", methods=["GET"])
def info():
    return jsonify({
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "endpoints": [
            {"method": "GET", "path": "/api/health"},
            {"method": "GET", "path": "/api/info"},
            {"method": "GET", "path": "/api/team"},
        ],
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

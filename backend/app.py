import os

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_NAME = "teamboard-backend"
SERVICE_VERSION = "1.0.0"


def get_db_connection():
    return psycopg2.connect(
        host=os.environ["POSTGRES_HOST"],
        port=os.environ.get("POSTGRES_PORT", "5432"),
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )


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

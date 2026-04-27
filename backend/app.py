import os

import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

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


@app.route("/api/team", methods=["GET"])
def team():
    try:
        conn = get_db_connection()
    except psycopg2.Error as exc:
        app.logger.error("DB connection failed: %s", exc)
        return jsonify({"error": "database unavailable"}), 503

    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT nombre, apellido, legajo, feature, servicio, estado "
                "FROM members"
            )
            rows = cur.fetchall()
    except psycopg2.Error as exc:
        app.logger.error("DB query failed: %s", exc)
        return jsonify({"error": "database query failed"}), 500
    finally:
        conn.close()

    members = [
        {
            "nombre": nombre,
            "apellido": apellido,
            "legajo": legajo,
            "feature": feature,
            "servicio": servicio,
            "estado": estado,
        }
        for (nombre, apellido, legajo, feature, servicio, estado) in rows
    ]
    return jsonify(members)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

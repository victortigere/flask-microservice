from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/match/health")
def auth_health():
    return jsonify({
        "status": "Auth Service Health"
    })


@app.route("/match/get/gigs")
def get_gigs():
    return jsonify({
        "code": "00",
        "description": "Fetched gigs successfully",
        "data": ""
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

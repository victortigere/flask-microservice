from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route("/monitor/health")
def monitor_health():
    return jsonify({
        "status": "Monitor Health"
    })


@app.route("/monitor/get/gigs")
def get_gigs():
    # make requests to matching service
    try:
        message = requests.get(
            "http://gig_matching_service:5001/match/get/gigs")
        return jsonify({"data": message.json()['description']})
    except requests.exceptions.RequestException as e:
        return jsonify({
            "code": "01",
            "description": "Could not process your request",
            "error": str(e)
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

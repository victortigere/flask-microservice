from flask import Flask, jsonify
import socket

app = Flask(__name__)


@app.route("/health")
def get_api_status():
    return jsonify({
                   "code": 00,
                   "description": "API status"})


@app.route("/details")
def get_details():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return jsonify({
        "hostname": str(host_name),
        "host_ip": str(host_ip)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

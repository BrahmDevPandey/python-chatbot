from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello there! Send requests to /bot to get responses'

@app.route("/bot", methods=["POST", "GET"])
def response():
    query = "" + dict(request.form)['query']
    result = query + " " + time.ctime()
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5500")
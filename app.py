from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import time
import getAnswer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return 'Send requests to /bot to get responses'

@app.route("/bot", methods=["POST", "GET"])
def response():
    query = dict(request.form)['query']
    result = getAnswer.getReply(query) + " " + time.ctime()
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5500")

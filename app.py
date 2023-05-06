# # Test client for interacting with Rasa bot

# import requests
# import os

# sender = input("What is your name?\n")
# bot_message = ""
# while bot_message != "Bye":
# 	message = input("What's your message?\n")

# 	print("Sending message now...")

# 	r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": sender, "message": message})

# 	print("Bot says, ")
# 	for i in r.json():
# 		bot_message = i['text']
# 		print(f"{i['text']}")

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/')
@cross_origin()
def hello_world():
    return 'Send requests to /bot to get responses'

@app.route("/bot", methods=["POST", "GET"])
def response():
    
    # query = dict(request.form)['query']
    query = request.json['query']
    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "aman", "message": query})
    result = []
    for i in r.json():
        result.append({"text" : i['text']})
    return jsonify(result)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5500")
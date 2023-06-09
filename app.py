"""Serves as an api to communicate with CheopsBot on Poe"""
import os
import logging
from flask import Flask, request
import poe

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

client = poe.Client(os.environ.get("POE_TOKEN"))


@app.route("/")
def get_home():
    """Just a sign that the server works"""
    return "It works"


@app.route("/send_message", methods=["POST"])
def send_message():
    """A method to communicate with CheopsBot on Poe"""
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        json = request.get_json()
        message = json["message"]
        print(message)
        response = client.send_message("cheopsbot", message, timeout=90)
        reply = ""

        for chunk in response:
            reply += chunk["text_new"]

        return reply

    return "Content-Type not supported!"


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

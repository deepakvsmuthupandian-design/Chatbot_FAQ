"""
Main file:
Runs the Flask FAQ chatbot application.
"""

from flask import Flask
from controller import ChatController

app = Flask(__name__)

controller = ChatController()


@app.route("/")
def index():
    return controller.index()


@app.route("/chat", methods=["POST"])
def chat():
    return controller.chat()


@app.route("/topics", methods=["GET"])
def topics():
    return controller.topics()


if __name__ == "__main__":
    print("FAQ Chatbot is running...")
    print("Open this link in browser: http://127.0.0.1:5000")

    app.run(debug=True)
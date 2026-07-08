"""
Controller file:
Handles requests from the user and gets answers from model.py.
"""

from flask import render_template, request, jsonify
from model import FAQModel


class ChatController:

    def __init__(self):
        self.model = FAQModel()

    def index(self):
        return render_template("index.html")

    def chat(self):
        data = request.get_json()

        if not data:
            return jsonify({
                "response": "Invalid request."
            }), 400

        user_message = data.get("message", "").strip()

        if user_message == "":
            return jsonify({
                "response": "Please type a question."
            }), 400

        answer = self.model.find_best_match(user_message)

        return jsonify({
            "response": answer
        })

    def topics(self):
        return jsonify({
            "topics": self.model.get_all_topics()
        })
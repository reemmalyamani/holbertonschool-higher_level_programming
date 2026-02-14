#!/usr/bin/python3
"""
Task 04: Simple API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory:
# key = username, value = full user object (dict)
# NOTE: Do NOT include testing data here !!.
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return a JSON list of all usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # If body is not valid JSON -> 400 Invalid JSON
    data_in = request.get_json(silent=True)
    if data_in is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data_in.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the whole object as the value
    users[username] = {
        "username": username,
        "name": data_in.get("name"),
        "age": data_in.get("age"),
        "city": data_in.get("city"),
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # Flask dev server
    app.run()


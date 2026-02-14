#!/usr/bin/python3
"""
Task 05: API Security and Authentication Techniques
- Basic Auth with Flask-HTTPAuth
- JWT Auth with Flask-JWT-Extended
- Role-based access control (admin-only)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)


app = Flask(__name__)

# Secret key for JWT (keep simple for the exercise; in real apps use env vars)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users store (as specified)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# -------------------------
# Basic Authentication
# -------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error():
    # Basic auth failures should be 401
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -------------------------
# JWT Error Handlers (MUST return 401)
# -------------------------
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_required(err):
    return jsonify({"error": "Fresh token required"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


# -------------------------
# JWT Authentication
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        # Not specified explicitly, but sensible; keeps behavior consistent
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Put identity info (including role) inside the token payload via identity
    identity = {"username": username, "role": user["role"]}
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    # identity is the dict we stored in create_access_token
    role = identity.get("role") if isinstance(identity, dict) else None

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()


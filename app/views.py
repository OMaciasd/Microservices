from flask import Blueprint, request, jsonify
import jwt
import os
import pathlib

env_path = pathlib.Path(__file__).parent.parent / 'config' / '.env'

with open(env_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value

API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

if not API_KEY:
    raise ValueError("API_KEY is not set.")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set.")

main = Blueprint('main', __name__)

@main.route('/generate-jwt', methods=['GET'])
def generate_jwt_endpoint():
    payload = {"user": "example_user"}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

@main.route('/DevOps', methods=['POST', 'GET', 'PUT', 'DELETE', 'PATCH'])
def devops_endpoint():
    if request.method != 'POST':
        return "ERROR", 405

    received_api_key = request.headers.get("X-Parse-REST-API-Key")
    print(f"Received API Key: {received_api_key}")

    if not received_api_key == API_KEY:
        return "ERROR: Invalid API Key", 401

    jwt_header = request.headers.get("X-JWT-KWY")
    if not jwt_header:
        return "ERROR: Missing JWT Header", 400

    try:
        decoded_payload = jwt.decode(jwt_header, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "ERROR: JWT Token has expired", 401
    except jwt.InvalidTokenError:
        return "ERROR: Invalid JWT Token", 401

    if decoded_payload["user"] != "example_user":
        return "ERROR: Unauthorized user", 401

    data = request.json
    if not all(field in data for field in ["message", "to", "from", "timeToLifeSec"]):
        return jsonify({"error": "Incorrect Payload"}), 400

    return jsonify({
        "message": f"Hello {data['to']} your message will be send"
    }), 200

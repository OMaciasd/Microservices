from flask import Flask, request, jsonify
import jwt
import uuid
import datetime

app = Flask(__name__)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
SECRET_KEY = "supersecret"

@app.route('/generate-jwt', methods=['GET'])
def generate_jwt_endpoint():
    payload = {
        "user": "example_user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600),
        "transaction_id": str(uuid.uuid4())  # Genera un UUID para cada transacción
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"jwt": encoded_jwt})

@app.route('/DevOps', methods=['POST', 'GET', 'PUT', 'DELETE', 'PATCH'])
def devops_endpoint():
    if request.method != 'POST':
        return "ERROR", 405

    received_api_key = request.headers.get("X-Parse-REST-API-Key")
    if not received_api_key == API_KEY:
        return "ERROR: Invalid API Key", 401

    jwt_header = request.headers.get("X-JWT-KWY")
    if not jwt_header:
        return "ERROR: Missing JWT Header", 400

    # Decodificar y validar JWT
    try:
        decoded_payload = jwt.decode(jwt_header, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "ERROR: JWT Token has expired", 401
    except jwt.InvalidTokenError:
        return "ERROR: Invalid JWT Token", 401

    # Aquí verificamos el usuario en el JWT
    if decoded_payload["user"] != "example_user":
        return "ERROR: Unauthorized user", 401

    data = request.json
    if not all(field in data for field in ["message", "to", "from", "timeToLifeSec"]):
        return jsonify({"error": "Incorrect Payload"}), 400

    return jsonify({
        "message": f"Hello {data['to']} your message will be send"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

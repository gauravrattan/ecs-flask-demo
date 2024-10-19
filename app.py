from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy token for demonstration purposes
VALID_TOKEN = "your_secret_token"

# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from guys in the cloud!"}), 200

# Private API endpoint
@app.route('/private', methods=['GET'])
def private():
    token = request.headers.get('Authorization')

    if token == f"Bearer {VALID_TOKEN}":
        return jsonify({"message": "This is a private message!"}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

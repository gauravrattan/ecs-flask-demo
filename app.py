from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from guys in the cloud!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

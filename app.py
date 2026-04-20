from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "message": "Application is running"}), 200

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!", "author": "DevOps CI/CD"}), 200

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        "app_name": "DevOps Sample App",
        "version": "1.0.0",
        "endpoints": ["/health", "/hello", "/api/info"]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
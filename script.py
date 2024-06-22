from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

def hash_message(message):
    algorithms = {
        'md5': hashlib.md5(message.encode()).hexdigest(),
        'sha1': hashlib.sha1(message.encode()).hexdigest(),
        'sha224': hashlib.sha224(message.encode()).hexdigest(),
        'sha256': hashlib.sha256(message.encode()).hexdigest(),
        'sha384': hashlib.sha384(message.encode()).hexdigest(),
        'sha512': hashlib.sha512(message.encode()).hexdigest(),
    }
    return algorithms

@app.route('/hash', methods=['POST'])
def hash_endpoint():
    if request.is_json:
        data = request.get_json()
        if 'message' in data:
            message = data['message']
            hashed_results = hash_message(message)
            return jsonify(hashed_results)
    return jsonify({"error": "Invalid request"}), 400

if __name__ == "__main__":
    app.run(debug=True)

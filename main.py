from flask import Flask, jsonify
import hashlib
import time

app = Flask(__name__)

@app.route('/get_token', methods=['GET'])
def get_token():
    token_key = int(time.time()*1000)*1000
    token_key_encode = (str(token_key)).encode('utf-8')
    token_key_hash = hashlib.sha256()
    token_key_hash.update(token_key_encode)
    data = {
        'status': 201,
		'token_key': str(token_key_hash.hexdigest())
    }
    
    return jsonify(data)

app.run(debug=True)
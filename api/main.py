from flask import Flask, jsonify, request
from flask_cors import CORS
import hashlib
import time
import redis
import json

from bd import DatabaseConnection

app = Flask(__name__)
CORS(app)

@app.route('/get_token', methods=['GET'])
def get_token():
    token_key = int(time.time()*1000)*1000
    token_key_encode = (str(token_key)).encode('utf-8')
    token_key_hash = hashlib.sha256()
    token_key_hash.update(token_key_encode)
    database = DatabaseConnection()
    token = str(token_key_hash.hexdigest())
    result = database.select(f"SELECT * FROM token WHERE token='{token}'")
    if len(result) == 0:
        database.query(f"INSERT INTO token (token) VALUES ('{token}')")
        data = {
            'status': 201,
            'token_key': str(token_key_hash.hexdigest())
        }
        return jsonify(data)
    else:
        data = {
            'status': 404
        }
        database.close()
        return jsonify(data)
    
@app.route('/get_notifications', methods=['GET'])
def get_notifications():
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    notifications = redis_client.lrange("notifications", 0, -1)
    redis_client.delete("notifications")
    print(notifications)
    notifications_json = [json.loads(item) for item in notifications]
    data = {
        "status": 200,
        "notifications": notifications_json
    }
    return jsonify(data)

@app.route('/seen_token', methods=['POST'])
def seen_token():
    data = request.get_json()
    token = data.get("token")
    database = DatabaseConnection()
    result = database.select(f"SELECT * FROM token WHERE token='{token}'")
    if len(result) == 0:
        redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
        ts = int(time.time()*1000)
        data_redis = {
            'ts': ts,
            'token_key': str(token)
        }
        redis_client.rpush("notifications", json.dumps(data_redis))
        redis_client.close()
        data = {
            'status': 200
        }
        database.close()
        return jsonify(data)
    else:
        data = {
            'status': 404
        }
        database.close()
        return jsonify(data)

app.run(host="0.0.0.0",debug=True)
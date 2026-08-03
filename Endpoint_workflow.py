from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
passwords_db = {}

@app.route('/')
def home():
    return "Welcome to the App"

@app.route('/health')
def health():
    return "App is running"

@app.route('/add', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
        
    passwords_db[username] = password
    return jsonify({"status": "success", "message": "User added successfully"}), 200

@app.route('/get/<username>', methods=['GET'])
def get_user(username):
    password = passwords_db.get(username)
    if not password:
        return jsonify({"error": f"Username '{username}' not found"}), 404
        
    return jsonify({"username": username, "password": password}), 200

@app.route('/delete/<username>', methods=['DELETE', 'GET'])
def delete_user(username):
    if username not in passwords_db:
        return jsonify({"error": f"Username '{username}' not found"}), 404
        
    del passwords_db[username]
    return jsonify({"status": "success", "message": f"User '{username}' deleted successfully"}), 200









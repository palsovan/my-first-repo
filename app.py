from flask import Flask, request, make_response, jsonify
from session_manager import SessionManager

app = Flask(__name__)
session_manager = SessionManager()

@app.route('/')
def index():
    session_id = session_manager.get_session_id_from_cookie(request.headers.get('Cookie'))
    
    if not session_id or not session_manager.get_session(session_id):
        session_id = session_manager.create_session()
        response = make_response("Welcome! New session created.")
        response.set_cookie('session_id', session_id, httponly=True, secure=True, samesite='Strict')
    else:
        session = session_manager.get_session(session_id)
        response = make_response(f"Welcome back! Your session data: {session['data']}")
    
    return response

@app.route('/set_data', methods=['POST'])
def set_data():
    session_id = session_manager.get_session_id_from_cookie(request.headers.get('Cookie'))
    if not session_id or not session_manager.get_session(session_id):
        return jsonify({"error": "No valid session"}), 401
    
    data = request.json
    for key, value in data.items():
        session_manager.update_session(session_id, key, value)
    
    return jsonify({"message": "Data updated successfully"})

@app.route('/get_data')
def get_data():
    session_id = session_manager.get_session_id_from_cookie(request.headers.get('Cookie'))
    if not session_id or not session_manager.get_session(session_id):
        return jsonify({"error": "No valid session"}), 401
    
    session = session_manager.get_session(session_id)
    return jsonify(session['data'])

@app.route('/logout')
def logout():
    session_id = session_manager.get_session_id_from_cookie(request.headers.get('Cookie'))
    if session_id:
        session_manager.delete_session(session_id)
    
    response = make_response("Logged out successfully")
    response.set_cookie('session_id', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
import uuid
from http.cookies import SimpleCookie
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            'created_at': datetime.now(),
            'last_accessed': datetime.now(),
            'data': {}
        }
        return session_id

    def get_session(self, session_id):
        if session_id in self.sessions:
            self.sessions[session_id]['last_accessed'] = datetime.now()
            return self.sessions[session_id]
        return None

    def update_session(self, session_id, key, value):
        if session_id in self.sessions:
            self.sessions[session_id]['data'][key] = value
            self.sessions[session_id]['last_accessed'] = datetime.now()

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def cleanup_expired_sessions(self, max_age_minutes=30):
        current_time = datetime.now()
        expired_sessions = [
            session_id for session_id, session in self.sessions.items()
            if (current_time - session['last_accessed']) > timedelta(minutes=max_age_minutes)
        ]
        for session_id in expired_sessions:
            del self.sessions[session_id]

    @staticmethod
    def create_session_cookie(session_id, max_age_minutes=30):
        cookie = SimpleCookie()
        cookie['session_id'] = session_id
        cookie['session_id']['httponly'] = True
        cookie['session_id']['secure'] = True  # Use this in production with HTTPS
        cookie['session_id']['samesite'] = 'Strict'
        cookie['session_id']['max-age'] = max_age_minutes * 60
        return cookie

    @staticmethod
    def get_session_id_from_cookie(cookie_string):
        cookie = SimpleCookie(cookie_string)
        return cookie.get('session_id').value if cookie.get('session_id') else None
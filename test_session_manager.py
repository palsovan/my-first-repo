import unittest
from session_manager import SessionManager
from datetime import datetime, timedelta
from time import sleep

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        self.session_manager = SessionManager()

    def test_create_session(self):
        session_id = self.session_manager.create_session()
        self.assertIsNotNone(session_id)
        self.assertIn(session_id, self.session_manager.sessions)

    def test_get_session(self):
        session_id = self.session_manager.create_session()
        session = self.session_manager.get_session(session_id)
        self.assertIsNotNone(session)
        self.assertIn('created_at', session)
        self.assertIn('last_accessed', session)
        self.assertIn('data', session)

    def test_update_session(self):
        session_id = self.session_manager.create_session()
        self.session_manager.update_session(session_id, 'test_key', 'test_value')
        session = self.session_manager.get_session(session_id)
        self.assertEqual(session['data']['test_key'], 'test_value')

    def test_delete_session(self):
        session_id = self.session_manager.create_session()
        self.session_manager.delete_session(session_id)
        self.assertNotIn(session_id, self.session_manager.sessions)

    def test_cleanup_expired_sessions(self):
        session_id = self.session_manager.create_session()
        self.session_manager.sessions[session_id]['last_accessed'] = datetime.now() - timedelta(minutes=31)
        self.session_manager.cleanup_expired_sessions(max_age_minutes=30)
        self.assertNotIn(session_id, self.session_manager.sessions)

    def test_create_session_cookie(self):
        session_id = self.session_manager.create_session()
        cookie = self.session_manager.create_session_cookie(session_id)
        self.assertIn('session_id', cookie)
        self.assertEqual(cookie['session_id'].value, session_id)
        self.assertTrue(cookie['session_id']['httponly'])
        self.assertTrue(cookie['session_id']['secure'])
        self.assertEqual(cookie['session_id']['samesite'], 'Strict')

    def test_get_session_id_from_cookie(self):
        session_id = self.session_manager.create_session()
        cookie = self.session_manager.create_session_cookie(session_id)
        cookie_string = cookie.output(header='', sep=';')
        retrieved_session_id = self.session_manager.get_session_id_from_cookie(cookie_string)
        self.assertEqual(session_id, retrieved_session_id)

if __name__ == '__main__':
    unittest.main()
import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, mock")

if __name__ == '__main__':
    unittest.main()
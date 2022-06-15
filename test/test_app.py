from email import header
from src.app import app
import unittest


class AppTestCase(unittest.TestCase):
    def setUp(self):
        """
            Create a Flask application configured for testing
        """
        self.test_app = app.test_client(self)

    def test_index_get(self):
        """
            GIVEN a Flask application configured for testing
            WHEN the '/' page is requested (GET)
            THEN check that the reponse is valid
        """
        response = self.test_app.get('/')
        status_code = response.status_code
        content_type = response.content_type
        data = response.data
        self.assertEqual(status_code, 200)
        self.assertEqual(content_type, 'text/html; charset=utf-8')
        self.assertEqual(data, b'<p>Hello, World</p>')

    def test_index_get_with_accept_header(self):
        """
            GIVEN a Flask application configured for testing
            WHEN the '/' page is requested (GET) with the header 'Accept' set to 'application/json'
            THEN check that the reponse is valid
        """
        response = self.test_app.get(
            '/', headers={'Accept': 'application/json'})
        status_code = response.status_code
        content_type = response.content_type
        data = response.json
        self.assertEqual(status_code, 200)
        self.assertEqual(content_type, 'application/json')
        self.assertEqual(data, {"message": "Hello, World"})

    def test_index_post(self):
        """
            GIVEN a Flask application configured for testing
            WHEN the '/' page is requested (POST) with a request body
            THEN check that the reponse is valid
        """
        response = self.test_app.post('/', json={'name': 'Bob'})
        status_code = response.status_code
        content_type = response.content_type
        data = response.json
        self.assertEqual(status_code, 200)
        self.assertEqual(content_type, 'application/json')
        self.assertEqual(data, {"message": "Hello, Bob"})

    def test_index_post_without_parameters(self):
        """
            GIVEN a Flask application configured for testing
            WHEN the '/' page is requested (POST) without any request body
            THEN check that the reponse is valid and is failing
        """
        response = self.test_app.post('/')
        status_code = response.status_code
        content_type = response.content_type
        data = response.data
        self.assertEqual(status_code, 400)
        self.assertEqual(content_type, 'text/html; charset=utf-8')
        self.assertIn(b'400 Bad Request', data)


if __name__ == "__main__":
    unittest.main()

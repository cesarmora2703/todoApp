from flask_testing import TestCase
from flask import current_app, url_for
from app.config import Config
from app import create_app
import sys
sys.path.insert(0, '/Volumes/develMac/venv/todoApp')


class MainTest(TestCase):
    def create_app(self):

        app = create_app()

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self):
        response = self.client.get(url_for('index'))

        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)

        self.assertRedirects(response, url_for('index'))

"""
This module defines the test cases for all views
"""
# pylint: disable=cyclic-import
# pylint: disable=import-error
import http

from department_app import create_app
from department_app.models.employee import Employee
from department_app.tests.conftest import BaseTestCase


class TestBaseView(BaseTestCase):
    """
    This is the class for home_page view test case
    """

    def test_home_page(self):
        """
        Testing home_page accessibility without authorization
        """
        client = create_app().test_client()
        url = '/home'
        response = client.get(url)
        assert response.status_code == http.HTTPStatus.OK

    def test_register(self):
        """
        Testing login accessibility without authorization
        """
        client = create_app().test_client()
        url = '/register'
        response = client.get(url)
        assert response.status_code == http.HTTPStatus.OK

    def test_login(self):
        """
        Testing login accessibility without authorization
        """
        client = create_app().test_client()
        url = '/login'
        response = client.get(url)
        assert response.status_code == http.HTTPStatus.OK


class TestAuth(BaseTestCase):
    """
    This is the class for auth test cases
    """

    def test_success_register(self):
        """
        Testing the possibility of user registration
        """
        with create_app().test_client() as client:
            response = client.post('/register', data={
                'username': 'new_test',
                'email': 'new@test.com',
                'first_name': 'New',
                'last_name': 'Test',
                'password': 'newP@ss',
                'confirm_password': 'newP@ss'
            }, follow_redirects=True)

        # response does not depend on context, so can be tested outside the block
        assert response.status_code == http.HTTPStatus.OK

        self.assertTrue(Employee.is_authenticated)

    def test_success_login(self):
        """
        Testing the possibility of user logging in
        """
        with create_app().test_client() as client:
            response = client.post('/login', data={
                'email': 'somebody@test.com',
                'password': '1234567',
            }, follow_redirects=True)

        assert response.status_code == http.HTTPStatus.OK

        self.assertTrue(Employee.is_authenticated)

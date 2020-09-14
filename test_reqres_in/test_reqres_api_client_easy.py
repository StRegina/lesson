import requests
from unittest import TestCase

class TestReqresApiClient(TestCase):

    base_path = 'https://reqres.in/api/'

    def test_get_delayed_response(self):
        response = requests.get(f'{self.base_path}users?delay=3')
        return response

    def test_get_list_resourse(self):
        response = requests.get('https://reqres.in/api/unknown/')
        return response

    def test_get_list_users(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        return response

    def test_get_single_resourse(self):
        response = requests.get('https://reqres.in/api/unknown/2')
        return response

    def test_get_single_resourse_not_found(self):
        response = requests.get('https://reqres.in/api/unknown/23')
        return response

    def test_get_single_users(self):
        response = requests.get('https://reqres.in/api/users/2')
        return response

    def test_get_single_users_not_found(self):
        response = requests.get('https://reqres.in/api/users/23')
        return response

    def test_delete_user(self):
        response = requests.delete('https://reqres.in/api/users/2')
        return response

    def test_post_create(self):
        pload = {"name": "morpheus", "job": "leader"}
        response = requests.post('https://reqres.in/api/users', data=pload)
        return response

    def test_post_create(self):
        pload = {"name": "morpheus", "job": "leader"}
        response = requests.post('https://reqres.in/api/users', data=pload)
        return response

    def test_post_login_successful(self):
        pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = requests.post('https://reqres.in/api/login', data=pload)
        return response

    def test_post_login_unsuccessful(self):
        pload = {"email": "peter@klaven"}
        response = requests.post('https://reqres.in/api/login', data=pload)
        return response

    def test_post_register_successful(self):
        pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post('https://reqres.in/api/register', data=pload)
        return response

    def test_post_register_unsuccessful(self):
        pload = {"email": "sydney@fife"}
        response = requests.post('https://reqres.in/api/register', data=pload)
        return response

    def test_put_create(self):
        pload = {"name": "morpheus", "job": "zion resident"}
        response = requests.put('https://reqres.in/api/users/2', data=pload)
        return response

    def test_patch_update(self):
        pload = {"name": "morpheus", "job": "zion resident"}
        response = requests.patch('https://reqres.in/api/users/2', data=pload)
        return response
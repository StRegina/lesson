# Добавляем все в консоль, потом добавляем ReqresApiClient.get_delayed_response() и получаем ответ и так со всеми функциями
import requests
class ReqresApiClient:

    base_path = 'https://reqres.in/api/'

    def get_delayed_response(self):
        response = requests.get(f'{self.base_path}users?delay=3')
        return response

    def get_list_resourse():
        response = requests.get(base_path+'unknown')
        return response

    def get_list_users():
        response = requests.get('https://reqres.in/api/users?page=2')
        return response

    def get_single_resourse():
        response = requests.get('https://reqres.in/api/unknown/2')
        return response

    def get_single_resourse_not_found():
        response = requests.get('https://reqres.in/api/unknown/23')
        return response

    def get_single_users():
        response = requests.get('https://reqres.in/api/users/2')
        return response

    def get_single_users_not_found():
        response = requests.get('https://reqres.in/api/users/23')
        return response

    def delete_user():
        response = requests.delete('https://reqres.in/api/users/2')
        return response

    def post_create():
        pload = {"name": "morpheus", "job": "leader"}
        response = requests.post('https://reqres.in/api/users', data=pload)
        return response

    def post_create():
        pload = {"name": "morpheus", "job": "leader"}
        response = requests.post('https://reqres.in/api/users', data=pload)
        return response

    def post_login_successful():
        pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = requests.post('https://reqres.in/api/login', data=pload)
        return response

    def post_login_unsuccessful():
        pload = {"email": "peter@klaven"}
        response = requests.post('https://reqres.in/api/login', data=pload)
        return response

    def post_register_successful():
        pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post('https://reqres.in/api/register', data=pload)
        return response

    def post_register_unsuccessful():
        pload = {"email": "sydney@fife"}
        response = requests.post('https://reqres.in/api/register', data=pload)
        return response

    def put_create():
        pload = {"name": "morpheus", "job": "zion resident"}
        response = requests.put('https://reqres.in/api/users/2', data=pload)
        return response

    def test_patch_update():
        pload = {"name": "morpheus", "job": "zion resident"}
        response = requests.patch('https://reqres.in/api/users/2', data=pload)
        return response
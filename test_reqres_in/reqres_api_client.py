# Добавляем в консоль по очереди
# from test_reqres_in.reqres_api_client import ReqresApiClient - папка в котором хранится документ и сам документ
# client=ReqresApiClient() - создаем клиента
# resp=client.get_delayed_response() - у каждой функции свой метод

import requests
class ReqresApiClient:

    def __init__(self):
        self.base_path = 'https://reqres.in/api/'

    def request(self, method:str, path:str, data=None):
        url = self.base_path + path
        response = requests.request(method, url)
        return response

    def get_delayed_response(self):
        response = self.request('GET', 'users?delay=3')
        return response

    def get_list_resourse(self):
        response = self.request('GET', 'unknown')
        return response

    def get_list_users(self):
        response = self.request('GET', 'users?page=2')
        return response

    def get_single_resourse(self):
        response = self.request('GET', 'unknown/2')
        return response

    def get_single_resourse_not_found(self):
        response = self.request('GET', 'unknown/23')
        return response

    def get_single_users(self):
        response = self.request('GET', 'users/2')
        return response

    def get_single_users_not_found(self):
        response = self.request('GET', 'users/23')
        return response

    def delete_user(self):
        response = self.request('DELETE', 'users/2')
        return response

    def post_create(self):
        pload = {"name": "morpheus", "job": "leader"}
        response = self.request('POST','users', data=pload)
        return response

    def post_login_successful(self):
        pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = self.request('POST','login', data=pload)
        return response

    def post_login_unsuccessful(self):
        pload = {"email": "peter@klaven"}
        response = self.request('POST','login', data=pload)
        return response

    def post_register_successful(self):
        pload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = self.request('POST','register', data=pload)
        return response

    def post_register_unsuccessful(self):
        pload = {"email": "sydney@fife"}
        response = self.request('POST','register', data=pload)
        return response

    def put_create(self):
        pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request('PUT','users/2', data=pload)
        return response

    def patch_update(self):
        pload = {"name": "morpheus", "job": "zion resident"}
        response = self.request('PATCH','users/2', data=pload)
        return response
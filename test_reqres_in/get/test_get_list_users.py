import requests
def test_get_list_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    if response.status_code == 200:
        return response.json()
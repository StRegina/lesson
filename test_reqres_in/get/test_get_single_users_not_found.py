import requests
def test_get_single_users_not_found():
    response = requests.get('https://reqres.in/api/users/23')
    if response.status_code == 404:
        return response.json()
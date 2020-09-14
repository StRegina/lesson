import requests
def test_get_single_users():
    response = requests.get('https://reqres.in/api/users/2')
    if response.status_code == 200:
        return response.json()
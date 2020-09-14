import requests
def test_get_delayed_response():
    response = requests.get('https://reqres.in/api/users?delay=3')
    if response.status_code == 200:
        return response.json()
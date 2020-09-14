import requests
def test_post_login_successful():
    pload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post('https://reqres.in/api/login', data=pload)
    if response.status_code == 200:
        return response.json()
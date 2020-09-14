import requests
def test_post_create():
    pload = {"name": "morpheus", "job": "leader"}
    response = requests.post('https://reqres.in/api/users', data=pload)
    if response.status_code == 201:
        return response.json()
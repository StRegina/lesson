import requests
def test_get_single_resourse():
    response = requests.get('https://reqres.in/api/unknown/2')
    if response.status_code == 200:
        return response.json()
import requests
def test_get_single_resourse_not_found():
    response = requests.get('https://reqres.in/api/unknown/23')
    if response.status_code == 404:
        return response.json()
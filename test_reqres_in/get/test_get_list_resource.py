import requests
def test_get_list_resourse():
    response = requests.get('https://reqres.in/api/unknown')
    if response.status_code == 200:
        return response.json()
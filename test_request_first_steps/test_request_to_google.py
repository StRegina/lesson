import requests
def test_get():
    response = requests.get('https://www.google.com/')
    if response.status_code == 200:
        print('Good')
    elif response.status_code == 404:
        print('Bad')
import requests
def ttest_post_register_unsuccessful():
    pload = {"email": "sydney@fife"}
    response = requests.post('https://reqres.in/api/register', data=pload)
    if response.status_code == 400:
        return response.json()
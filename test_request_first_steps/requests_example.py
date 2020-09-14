import requests
r = requests.get('https://www.google.com/')
r
r.status_code
r.text
print(r.url)
r.encoding
r.json()
r.headers
import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
secont_response = response

print(first_response.url)
print(secont_response.url)
#print(response.status_code)
#print(response.text)
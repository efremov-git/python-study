###api_hello###
import requests

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name":"User"})
parsed_response_text = response.json()
print(parsed_response_text["answer"])


###get_text###
#from json.decoder import JSONDecodeError
#import requests

#response = requests.get("https://playground.learnqa.ru/api/get_text")
#print(response.text)

#try:
#    parsed_response_text = response.json()
#    print(parsed_response_text)
#except JSONDecodeError:
#    print("Response is not a JSON format")


###get300-500###
#import requests

#response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#first_response = response.history[0]
#secont_response = response

#print(first_response.url)
#print(secont_response.url)
##print(response.status_code)
##print(response.text)


###check_type###
#import requests

#response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
#print(response.text)



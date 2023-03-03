import requests

response = requests.get("https://playground.learnqa.ru/api/check_type")
print(parsed_response_text["answer"])
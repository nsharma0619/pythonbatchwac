import requests

response = requests.get("https://en.wikipedia.org/wiki/Constitution_of_India")
response_data = response.text


print(response_data)
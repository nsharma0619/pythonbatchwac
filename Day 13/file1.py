import requests

response = requests.get("https://currencyapi.net/api/v1/rates?key=NXtUyotjncqJie5GKVEjlBi6FYfjgQuQyjjL&base=USD")
response_json = response.json()


one_dollar_value = float(response_json["rates"]["INR"])
x_dollar = int(input())

print(one_dollar_value*x_dollar)
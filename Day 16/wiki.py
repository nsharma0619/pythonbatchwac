import requests
from bs4 import BeautifulSoup

topic = input("Enter the topic to search : ")
# constitution_of_india
modified_topic = ""
for i in topic:
    if i==" ":
        modified_topic+='_'
    else:
        modified_topic+=i

url = "https://en.wikipedia.org/wiki/" + modified_topic
response = requests.get(url)

html_data = response.text
soup = BeautifulSoup(html_data, 'html.parser')

print(soup.text)

# https://www.tutorialspoint.com/flask/index.htm
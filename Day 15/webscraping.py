from bs4 import BeautifulSoup
import requests 

response = requests.get('https://www.oreilly.com/library/view/python-cookbook/0596001673/ch06s03.html')

html_data = response.text
soup = BeautifulSoup(html_data, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
# print(soup.find_all('a'))
print(soup.get_text())
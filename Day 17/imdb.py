import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

def get_ids(n):
    df = pd.read_csv('links.csv')
    movie_ids = list(df['imdbId'])
    return movie_ids[0:n]

def scrap(id):
    url = "https://www.imdb.com/title/tt{}".format(str(id).zfill(7))
    response = requests.get(url)
    html_data = response.text
    soup = BeautifulSoup(html_data, 'html.parser')
    info = soup.find('script', attrs={"type":"application/ld+json"})
    info = info.string
    json_data = json.loads(info)
    movie = {
        "name":json_data['name'],
        "genre":json_data['genre'],
        "image":json_data['image'],
        "description" : json_data['description']
    }
    return movie


ids = get_ids(5)
for i in ids:
    movie_info = scrap(i)
    print(movie_info)



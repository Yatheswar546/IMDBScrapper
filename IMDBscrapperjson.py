from bs4 import BeautifulSoup
import requests
import json

data = []

try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    
    for movie in movies:

        name =  movie.find('td', class_="titleColumn").a.get_text()

        # rank = movie.find('td', class_="titleColumn").text

        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]

        year = movie.find('td', class_="titleColumn").span.text.strip('()')

        rating = movie.find('td', class_="ratingColumn imdbRating").strong.get_text()

        # print(int(rank), name, int(year), float(rating))
        movie_data = {
            'Rank of Movie' : int(rank),
            'Movie Title': name,
            'Year of Release': year,
            'Rating': rating
        }

        data.append(movie_data)

    with open('Top IMDB Rating Movies.json','w') as json_file:
        json.dump(data, json_file, indent=4)

except Exception as e:
    print(e)


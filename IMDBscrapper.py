from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies from IMDB'
sheet.append(['Rank of Movie','Movie Title','Released Year','IMDB Rating'])

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
        sheet.append([int(rank), name, int(year), float(rating)])

except Exception as e:
    print(e)

excel.save('IMDB Ratings.xlsx')
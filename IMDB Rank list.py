from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.imdb.com/chart/top"
request = requests.get(url)

soup = BeautifulSoup(request.content, "lxml")

top_250 = soup.find("tbody" ,attrs={"class":"lister-list"}).findAll("tr")

film_sira = 1
print("Welcome to İMDB Top 250 Film List")
print("-----------------------------------")
for film in top_250:
    adi = film.find("td" ,attrs={"class":"titleColumn"}).a.text
    yili = film.find("td" ,attrs={"class":"titleColumn"}).span.text
    puan = film.find("td" ,attrs={"class":"ratingColumn imdbRating"}).strong.text
    print(str(film_sira) + '.')
    print("name: ", adi)
    print("year: ", yili)
    print("rank: ", puan)
    
    print("\n")
    film_sira += 1
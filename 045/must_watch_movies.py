from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empireonline_web_page = response.text

soup = BeautifulSoup(empireonline_web_page, "html.parser")

movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_list = [movie.getText() for movie in movies]

with open("045\movies.txt", mode="w") as file:
    for movie in reversed(movie_list):
        file.write(f"{movie}\n")

# alternative way of creating a list in reverse order
# movies = movie_list[::-1]
# print(movies)

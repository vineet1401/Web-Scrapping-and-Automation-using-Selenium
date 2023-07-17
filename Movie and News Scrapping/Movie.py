import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable

response = requests.get(url="https://www.imdb.com/list/ls051594496/")
content = response.text 

soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify())

movie_name = soup.select(".lister-item-header a")
movie_year = soup.select(".lister-item-header span")


movies = [[], []]

j = 0
for i in range(0, len(movie_year),2 ):
    movies[0].append(movie_name[j].get_text())
    movies[1].append(movie_year[i+1].get_text())
    j += 1

t = PrettyTable(['Sr. No', 'Name', 'Year'])
for i in range(0, len(movie_name)):
    t.add_row([i+1, movies[0][i], movies[1][i]])

print(t)


# df = pd.DataFrame(movies_to_display)
# # dfStyler = df.style.set_properties(**{'text-align': 'left'})
# # dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
# print(df)
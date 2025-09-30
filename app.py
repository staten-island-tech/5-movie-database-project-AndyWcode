import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

#file 1
# for movie in data:
#     print(movie["title"])

#file 2

useryear = input(" What Year of movies do you want: ")

for movie in data:
    if movie["year"] <= useryear:
        print(movie["titl"])
import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

#file 1
# for movie in data:
#     print(movie["title"])

#file 2

# useryear = int(input(" What Year of movies do you want: "))

# for movie in data:
#     if movie["year"] <= useryear:
#         print(movie["title"])

#file 3

# useryear = int(input("Movies released after:  "))
# useryearbefore = int(input("Movies released before "))

# for movie in data:
#     if movie["year"] <= useryear and movie["year"] >= useryearbefore:
#         print(movie["title"])
                     

#file 4

# useryear = int(input("What year of movies do u want: "))

# for movie in data:
#     if movie["year"] == useryear:
#         print(movie["title"

#file 5
# def movie_finder():

#     usermovie = input("WHAT MOVIE U WANT: ")
#     for movie in data:
#         if movie["title"] == usermovie:
#             print("Movie found!")
#             print(usermovie)

#file 6 
def movie_genre():
    usergenrelist = []
    while True: 
        usergenre = input("What genre you want?: ")
        if usergenre == "N":
            print(f" You search for movies with the genre {usergenrelist}")
            for movie in data:
                if usergenrelist == movie["genres"]:
                    print(movie["title"])
        else:
            usergenrelist.append(usergenre)

           
movie_genre()

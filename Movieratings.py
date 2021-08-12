from imdb import IMDb

db = IMDb()

key = input("Enter Movie Name :- ")

movies = db.search_movie(key)
print(f'Searching for {key}:')

for movie in movies:
    title = movie['title']
    year = movie['year']
    print('')
    print(f'{title} -- {year}')

print('---------------------------------------')

id = movies[2].getID()
movie = db.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
print()
print('Movie info:')
print(f'{title} - {year}')
print(f'rating: {rating}')
print('---------------------------------------')


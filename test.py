from os import path

from PyMovieDb import IMDB
import json

imdb = IMDB()

with open("movies.csv", 'r') as fp:
    movieList = fp.readlines()

filename = "data.json"

if path.isfile(filename) is False:
  raise Exception("File not found")

with open(filename) as fp:
    jsonObj = json.load(fp)

for movie in movieList:
    res = imdb.get_by_name(movie, tv=False)
    data = json.loads(res)
    if not (data.get('review') is None):
        del data['review']
    if not (data.get('description') is None):
        del data['description']
    if not (data.get('actor') is None):
        del data['actor']
    if not (data.get('creator') is None):
        del data['creator']
    jsonObj.append(data)


with open(filename, 'w') as json_file:
    json.dump(jsonObj, json_file,
              indent=4,
              separators=(',', ': '))

print('Successfully appended to the JSON file')















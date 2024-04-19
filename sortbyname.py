import json

from os import path

import time

from PyMovieDb import IMDB

imdb = IMDB()


data_filename = "data.json"

if path.isfile(data_filename) is False:
    raise Exception("File not found")

with open(data_filename) as f:
    movieList = json.load(f)

movieNameList = [obj['name'] for obj in movieList if 'name' in obj]

print(movieNameList)

def track_time(sort, arr):
    start_time = time.perf_counter()
    sort(arr)
    end_time = time.perf_counter()
    print("The sorting algorithm took", abs(start_time - end_time), "seconds to run")


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key





track_time(insertion_sort, movieNameList)

print(movieNameList)


'''
filename = "sortedbyname.json"

jsonObj = []

for movie in movieNameList:
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
    if not (data.get('keywords') is None):
        del data['keywords']
    if not (data.get('director') is None):
        del data['director']
    jsonObj.append(data)


with open(filename, 'w') as json_file:
    json.dump(jsonObj, json_file,
              indent=4,
              separators=(',', ': '))

print('Successfully appended to the JSON file')

'''



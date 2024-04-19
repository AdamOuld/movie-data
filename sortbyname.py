import json

from os import path

import time

start_time = time.time()

filename = "data.json"

if path.isfile(filename) is False:
    raise Exception("File not found")

with open(filename) as f:
    movieList = json.load(f)

movieNameDict = [obj['name'] for obj in movieList if 'name' in obj]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertion_sort(movieNameDict)

print(movieNameDict)

print("This algorithm took", time.time() - start_time, "seconds to run")

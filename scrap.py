# Checking O(n) runtime for Arrays
# All of this code was originally written by Brady Fukamoto 
# Code is copied line by line by Mackenzie Weber

# O(n) to add to back
def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i+1)
    return x

# O(n^2) to add to front
def add_to_front(n):
    x = []
    for i in range(0, n):
        x.insert(0, n - i)
    return x 

import time

# O(n) for add to back
start_time = time.time()
add_to_back(15)
end_time = time.time()
print(f'runtime: {end_time - start_time} seconds')

# O(n^2) for add to front
start_time = time.time()
add_to_front(15)
end_time = time.time()
print(f'runtime: {end_time - start_time} seconds')

import hashlib

key = b'cats'

capacity = 8
print(key)
print(int(hashlib.sha256(key).hexdigest(), 16) % 8)
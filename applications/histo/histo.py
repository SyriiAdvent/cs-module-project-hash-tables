import re

with open("robin.txt") as f:
    words = f.read()

def word_count(s):
    cache = {}
    my_string = re.sub(r'[^A-Za-z0-9\' ]+', ' ', s).lower().split()

    for word in my_string:
        if word not in cache:
            cache[word] = '#'
        else:
            cache[word] += '#'
    return sorted(cache.items(), key=lambda x: x[1], reverse=True)


for word,rank in word_count(words):
  print(word, rank)

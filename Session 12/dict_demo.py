# Dictionaries

# Exercise 1
# Rewrite the function histogram using get.
# You should be able to eliminate the if statement.

def histogram(s):
    d = dict()              #empty dictonary
    for letter in s:             # for letter in string
        # if letter not in d:      # if letter is not in the keys of dictionary 
        #     d[letter] = 1        # dictionary value for that letter = 1
        # else:               # if key exists in dictionary
        #     d[letter] += 1       # add 1 to its value
    
        d[letter] = d.get(letter, 0) + 1    # same as if above but in one line
    return d                # returns each key (letter) and its value (how many times in word)

h = histogram("Bookeeper")
print(h)
# {'B': 1, 'o': 2, 'k': 1, 'e': 3, 'p': 1, 'r': 1}




# Random grades to students

# grades = {}
# import random
# for name in class_roster:
#     if name[0] == 'A':
#         grades[name] = random.randint(60, 100)
#     else:
#         grades[name] = random.randint(90, 100)



"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.
Among them, three are telling the truth while one is lying.
Could you find out who is the thief?
"""
# suspects = ['John', 'Paul', 'George', 'Ringo']

# for name in suspects:
#     if sum([
#         "John" != name,
#         "George" == name,
#         "Ringo" == name,
#         "Ringo" != name

import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'.format(
    city=city, country_code=country_code, APIKEY=APIKEY)

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?
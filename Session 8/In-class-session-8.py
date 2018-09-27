team = "New England Patriots"
# letter = team[19]
# print(letter)

# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index = index + 1
# # Another way
# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

team = 'New England Patriots'

# print(team[0:3]) #from index 0 to index 2 (3 not inclusive)
# print(team[0:4]) #from index 0 to index 3
# print(team[0:11])
# print(team[12:20]) #slicing the string (just one section fo the string)
# print(team[:11]) #same as [0:11]
# print(team[0:20:2]) #from index 0 to index 20 but only every 2 characters
# print(team[::2]) #same as above
# print(team[::-2]) #same as above but back to front

# #Strings are IMMUTABLE: they cannot be changed (you would need a new variable)

# new_team = team[:12]+'Beavers'
# print(new_team)
# print(team)

# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find(team, 'E'))

# for i in range(len(team)):
#     if team[i] == 'a':
#         print(i)

# for i, letter in enumerate(team):
#     if letter == 'a':
#         print(i, letter)

# word = 'New England Patriots'
# # count = 0
# # for letter in word:
# #     if letter == 'a':
# #         count = count + 1
# # print(count)

# def count(s, letter):
#     c = 0
#     for each in s:
#         if each == letter:
#             c += 1
#     return c

# print(count(team, 'a'))

# new_team = team.upper() #print team in uppercase letter
# print(new_team)

# print(team.split())
# print(team.split('e')) #gets rid of the e

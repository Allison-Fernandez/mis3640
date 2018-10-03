fin = open("mis3640/Session 9/words.txt")
# for line in fin:
#     word = line.strip()
#     print(word)

# counter = 0
# for line in fin:
#     word = line.strip()
#     counter += 1
#     #print(word)
# print(counter)

print('Exercise 1:')
print()
print('#1: Long words')
print()
# def read_long_words():
    # """
    # prints only the words with more than 20 characters
    # """

    # for line in fin:
    #     word = line.strip()
    #     if len(word) > 20:
    #         print(word)

# read_long_words()

print()
print()
print('#2: Has no "e"')
print()
# def has_no_e(word):
#     """
#     returns True if the given word doesn't have the letter "e" in it.
#     """

#     for letter in word:
#         if letter == 'e':
#             return False
#     return True

# print(has_no_e('Babson'))


# total_words = 113806

# def has_no_e_2():
#     counter = 0
#     for line in fin:
#         word = line.strip()
#         if has_no_e(word):
#             print(word)
#             counter += 1
            
                                
#     print(counter)
#     print('{:.4f}% of words have no "e".'.format((counter/total_words) * 100))

# has_no_e_2()


# print()
print('#3: Avoids')
print()
# def avoids(word, forbidden):
#     """
#     prints words that do not contain any of the letters given
#     """
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True

# print(avoids('Duele', 'Ricardo'))

# forbidden = input('Please neter 5 random letters: ')
# counter = 0
# def avoids_2():
#     for line in fin:
#         word = line.strip()        
#         for letter in word:
#             if letter not in forbidden:
#                 counter += 1
#                 print(word)

# avoids_2()

print()
print()
print('#4: Uses Only')

# def uses_only(word, allowed):
#     for letter in word:
#         if letter not in allowed:
#             return False
#     return True


# print(uses_only('carro', 'Ricardo'))


print()
print()
print('#5 ')

# def uses_all(word, required):
#     for letter in required:
#         if letter not in word:
#             return False
#     return True

# # print(uses_all('ricardo', 'carro'))

# def find_words_using_all_vowels():
#     counter = 0
#     for line in fin:
#         word = line.strip()
#         if uses_all(word, 'aeiou'):
#             print(word)
#             counter += 1
#     print(counter)


# find_words_using_all_vowels()

print()
print()
print('#6')


def is_abecedarian(word):
    previous = word[0]
    for letter in word:
        if letter < previous:
            return False
        previous = letter
    return True

print(is_abecedarian('aereo'))

def find_abecederian_words():
    counter = 0
    current_longer_word = ''
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            counter += 1
            if len(word)>len(current_longer_word):
                current_longer_word = word
                
    return counter, current_longer_word

print(find_abecederian_words())

print('Exercise 2:')
print()
print('#2: While')
print()


# def is_abecedarian_while(word):
#     previous = word[0]
#     while c in word < previous:
#         return True
#         previous += 1

# print(is_abecedarian_while('art'))
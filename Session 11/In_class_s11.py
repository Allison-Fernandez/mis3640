# t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x', 'y']
# print(t)

# t[1] = ['g', 'h']
# print(t)

# print(type(t[1]))


# List exercise discussion:

# def nested_sum(t):
#     total = 0 


t = [1, 2, 3]
def cumsum(t):
    total = 0
    res = []    #empty list that will be the filled with the new numbers and ultimatetly outputed
    for x in t:
        total += x
        res.append(total)  #add the total to the res list
    return res

print(cumsum(t))

def middle(t):
    return t[1:-1]

print(middle(t))

def is_sorted(t):
    # previous = t[0]
    # for item in t:
    #     if item < previous:
    #         return False
    #     previous = item
    # return True
    print(t.sort())
is_sorted([2, 1, 3, 4])


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram('stop', 'pots'))

def has_adjacent_duplicates(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

print(has_adjacent_duplicates('adbd'))
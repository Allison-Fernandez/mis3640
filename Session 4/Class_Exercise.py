# print(round(54.876542345678))
# print(min(3,76,234,876,345,8,2,8))
# print(ord('a'))
# print(chr('97'))

# def print_lyrics():
#     print("Hey Jude. Don't make it bad.")
#     print("Take a sad song and make it better.")

# print_lyrics()
# print(type(print_lyrics))

# def repeat_lyrics():
#     print_lyrics()
#     print('Na - na - na - na - na - na - na - na - na!')
#     print_lyrics()

# def print_twice(whatever):
#     print('first time:')
# print(whatever)
# print('the second time:')
# print(whatever)


# print_twice('Matthew')

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
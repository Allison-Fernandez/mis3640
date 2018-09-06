# Exercise 1
import math
r = 5
r_cube = 5 * 5 * 5
radius = (4/3)*(math.pi)*r_cube
print('1. The volume of a sphere with radius 5 is {:.2f}.'.format(radius))

# Exercise 2

book = 24.95 * .6
books = book * 60
shipping = 3 + .75 * 59
total_cost = books + shipping
print('2. The total wholesale cost for 60 books is ${:.2f}.'. format(total_cost))

# Exercise 3

minute = 60
pace = 8 * minute + 15
total_pace = 2 * pace
tempo = 7 * minute + 12
total_tempo = 3 * tempo
running = total_pace + total_tempo
running_minutes = running / 60
#  running time is 38 minutes and 6 seconds
breakfast = '7:30'
print('3. You will get home for breakfast at {} am.'.format(breakfast))

# Exercise 4

difference = 89 - 82
percent = difference / 82
difference = percent * 100
print('4. The percent increase in your grade is {:.1f}%.'.format(difference))
# result = 0

# for i in range(1,1001):
#     if i % 2 == 0:
#         result = result + i
# print('The sum of odd numers is', result)
#     # print('current numer to be added:',i)
#     result = result + i
#     # print('new result after this iteration:', result)

# print('The final result:', result)


# result = 0

# for i in range(1, 1001, 2):
#     result = result + i

# print('The sum of odd numbers if',result)


# result = 1

# for i in range (1, 11):
#     result = result * i

# print('The factorial of 10 is', result)


# import time

# def countdown(n):
#     while n>0:
#         print(n)
#         time.sleep(1)
#         n = n-1
#     print('Blastoff')

# countdown(5)



# while True:
#     print('press "q" to quit')
#     line = input('> ')
#     if line == 'q':
#         break
#     print(line)

# print('Done!')


import math
epsilon = 0.0000001

def mysqrt(a):
    print('a = {}' .format(a))
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    print('mysqrt = {}' .format(x))
    print('math sqrt = {}' .format (math.sqrt(a)))

for a in range (1, 10):
    mysqrt(a)
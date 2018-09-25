# age = input('please enter your age: ')

# if int(age) > 18:
#     print('adult')
# elif int(age) >= 6 :
#     print('teenager')
# else:
#     print('kid')

# weight = input ('enter your weight in kg ')
# height = input ('enter your height in meters ')
# def calculate_bmi (weight, height):
#     bmi = float(weight) / float(height)
#     print('{:.1f}'.format(bmi))

# if float (bmi) < 18.5:
#     print('underweight')
# elif 18.5 >= float (bmi) <= 24.9:
#     print ('normal weight')
# elif 25 <= float (bmi) <= 20.9:
#     print('overweight')
# else:
#     print('obese')

# calculate_bmi(weight,height)

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(2))
# print(fibonacci(6))

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

print(factorial(3))
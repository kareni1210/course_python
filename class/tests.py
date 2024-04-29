# La diferencia entre una lista y una tupla es que los elementos de la tupla son inmutable, es decir n o pueden
# modificarse
# my_tuple = (8, 9, 8)
# type(my_tuple)

# Verify the age of a person, if the age is less than 18 print 'you are a kid', otherwise print 'you are an adult'
"""age = int(input('What is your age?: '))  # Type casting
if age < 18:
    print("You're a kid")
else:
    print("You're an adult")
"""
# import random

#####################

"""books = ['spivak', 'apostol', 'bowers', 'stewart', 'mood']
resp = input('Tell me a famous math book: ').lower()
if resp in books and resp == 'spivak':
    print('You really know a lot ')
"""

#####################
"""x = 'spam'
while x:  # El x es permitido porque es un string no vacío, es un true
    print(x, end=' ')
    x = x[1:]
    """
#####################
"""x = 10
while x:
    x -= 1
    if x % 2 == 0:
        continue
    print(x)"""

# words = ['despair', 'phone', 'computer', 'english', 'science']
# print(dir(words))  # Te muestra los métodos usados en la clase
#
# x = 'hola'
# print(x[1])
#
# k = -len(words)
# while words:
#     print(words[k])  # Los corchetes se usan para acceder al indice i de un iterable
#     del words[k]
#     k += 1
#     print(words)

# SUM OF POSITIVE NUMBERS
# Objective: Write a program that repeatedly asks the user to enter a number.
# If the number is positive add it to a running total.
# If the number is negative, stop the loop and print the final total.
# suma = 0
# while True:
#     nu = int(input('Write a number: '))
#     if nu < 0:
#         print(suma)
#         break
#     suma += nu

########################

# FOR
# items = ['aaa', 111, (4, 5), 2.01, 3.14]
# tests = [(4, 5), 3.14]
# flag = True
# for key in tests:
#     for item in items:
#         if item == key:
#             break
#         else:
#             flag = True
#
# # Funciona solo para el último valor
#
# if flag:
#     print(key, 'was found')
# else:
#     print(key, 'was not found')

# listp = []
# while True:
#     a = bool(int(input('Do you want to add a number? (1 for yes, 0 for no): ')))
#     if a == 1:
#         nu = int(input('Write a number: '))
#         if nu % 2 == 0:
#             listp.append(nu)
#             continue
#     else:
#         break
# print(listp)

# listp = []
# while True:
#     nu = int(input('Write a number: '))
#     if nu % 2 == 0:
#         listp.append(nu)
#     a = bool(int(input('Do you want to continue? (1 for yes, 0 for no): ')))
#     if not a:
#         break
#
# print(listp)


#######################

# while True:
#     password = input('Enter the password: ')
#     if password == 'python123':
#         print(":) you're in")
#         break
#     else:
#         print(':( Try again...')

########################

# # Write a number to calculate the factorial of a given number
# num = int(input('Enter a number: '))
# fac = 1
# suma = 0
# if num == 0 | num == 1:
#     print(f'El factorial es:{fac} ')
# else:
#     for n in range(1, num+1):
#         suma += n * 1
#         fac = fac * n
#     print(fac)
#     print(suma)

#########################

# Clase 19/04/24
# people = ['F1', 'F2', 'A1', 'A2', 'A3', 'S1', 'S2', 'S3', 'S4']
# fellow = ['F1', 'F2']
# associates = ['A1', 'A2', 'A3']
# students = ['S1', 'S2', 'S3', 'S4']
#
# pos_result = []
#
# for m1 in people:
#     for m2 in people:
#         for m3 in people:
#             pos_result.append((m1, m2, m3))
#
# print(pos_result)
#
# cases_interest = []
# for f in fellow:
#     for a in associates:
#         for s in students:
#             cases_interest.append((f, a, s))
#             cases_interest.append((f, s, a))
#             cases_interest.append((a, f, s))
#             cases_interest.append((a, s, f))
#             cases_interest.append((s, a, f))
#             cases_interest.append((s, f, a))

#########################

# faces = []
# for f in range(1, 7):
#     faces.append(f)
#
# n = 100
# face_selected = 5
# occurrence = 0
# for _ in range(n):
#     random_face = random.choice(faces)
#     if face_selected == random_face:
#         occurrence += 1
#
# print(f'The frequency of face number {face_selected} in '
#       f'{n} trials is {occurrence / n}')

#####################

# faces = [f for f in range(1, 7)]
#
#
# def roll_dice():
#     return random.choice(faces)
#
#
# def rolling(r, face):
#     time = 0
#     for _ in range(r):
#         if roll_dice() == face:
#             time += 1
#     return time
#
#
# def frequency(r, face):
#     print(f'The frequency is: {rolling(r, face) / r}')
#
#
# n = int(input('How many trials do you want?: '))
# user_face = int(input('Which face?: '))
#
# frequency(n, user_face)

#######################

#
# def printing_things(a):
#     for _ in range(a):
#         print('   *   ')
#         print('  ***  ')
#         print(' ***** ')
#         print('   T   ')
#
#
# x = int(input('How many trees do you want?: '))
# printing_things(a)

########################

x = 45


def outer_function(var1):
    y = 12
    a = var1

    def inside_function():
        b = 17
        print(x, y, a, b)
    # print(b)
    inside_function()


# print(y)
outer_function(4)


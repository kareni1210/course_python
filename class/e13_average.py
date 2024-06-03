"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""

n = int(input('Enter a humber: '))
cont = 0
if n == 0:
    print('There are any values')
else:
    suma = n
    while n != 0:
        n = int(input('Enter a humber: '))
        cont += 1
        suma += n
    prom = suma/cont
    print(prom)

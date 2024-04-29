# Make a program that determines if a number (given by the user) is odd or even
# Users number
number = int(input('Enter a number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

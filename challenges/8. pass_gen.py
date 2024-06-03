import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numlet = int(input('How many letters would you like in your password? '))
nnumbers = int(input('How many numbers would you like in your password? '))
nsymbols = int(input('How many symbols would you like in your password? '))


def password(a, b, c):
    lista = []
    for _ in range(a):
        lista.append(random.choice(letters))
    for _ in range(b):
        lista.append(random.choice(numbers))
    for _ in range(c):
        lista.append(random.choice(symbols))
    random.shuffle(lista)
    lis2str = ""
    for y in lista:
        lis2str += y
    print(f'Your password is: {lis2str}')


password(numlet, nnumbers, nsymbols)

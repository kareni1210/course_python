# Write a program to find and print all prime numbers between 1 and 100

for num in range(1, 101):
    div = 0
    for com in range(1, 101):
        if num % com == 0:
            div += 1
    if div <= 2:
        print(num, end=' ')

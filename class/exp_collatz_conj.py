"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""
num = int(input('Enter a number: '))
if num == 1:
    print(num)
else:
    print(num)
    a = 0
    while num != 1:
        if num % 2 == 0:
            num = num/2
        elif num % 2 != 0:
            num = 3*num+1
        a += 1
        print(num)
    print(f'El número de operaciones que se necesitaron para llegar al 1 son {a}')

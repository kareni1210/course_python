# Generate and print the multiplication table (up to 10) for a given number
num = int(input('Enter a number: '))
mul = 0
for x in range(1, 11):
    mul = num * x
    print(f'{num} * {x} = {mul}')

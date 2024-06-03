# Import the math module (as you want)

import math


# Make the Poisson distribution. The user must enter the parameters. Then print out the result
lam = float(input('Enter the parameter lambda: '))
x = int(input('Enter the parameter x: '))
pois = (math.exp(-lam) * pow(lam, x)) / math.factorial(x)
print(pois)

# def pois(lam, x):
#     k = math.factorial(x)
#     e = math.exp(-lam)
#     dis = (e*pow(lam, x))/k
#     print(dis)
#
#
# pois(9, 2)


# Make an iterable with some numbers to calculate the product of all those numbers

a = [2, 4, 5, 6]
print(math.prod(a))

# From two iterables, calculate the sum of the product of values

a = [2, 4, 6]
b = [1, 3, 5]
print(math.sumprod(a, b))

# Calculate the GCD of two numbers that user gives

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the first number: '))
print(f'The greatest common divisor of both numbers is {math.gcd(n1, n2)}')

# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result

n = int(input('Enter the n value: '))
x = int(input('Enter the x value: '))
p = float(input('Enter the p value: '))
if 0 <= p <= 1:
    bi = math.comb(n, x)*pow(p, x)*pow(1-p, n-x)
    print(bi)
else:
    print("There doesn't exist probabilities bigger than 1 and smaller than 0")

# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "

fn = float(input('Enter a float number: '))
print(f'The ceiling of {fn} is {math.ceil(fn)}')

# Choose two functions from the math documentation to make exercises like the previous

"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""
# Una lambda function es una declaración de una función que se utilizará una sola vez


quad = lambda a, b, c: ((- b + pow((b ** 2) - 4 * a * c, 0.5))/(2 * a), (- b - pow((b ** 2) - 4 * a * c, 0.5))/(2 * a))
print(quad(2, 2, 0))

print((lambda a, b, c: (f'X1: {(- b + pow((b ** 2) - 4 * a * c, 0.5))/(2 * a)}',
                        f'X2: {(- b - pow((b ** 2) - 4 * a * c, 0.5))/(2 * a)}'))
      (2, 2, 0))

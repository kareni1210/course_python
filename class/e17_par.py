# re = range(1, 10, 2)  # Using positional only
#
#
# # Defining a function with positional only
# def func1(value1, value2, value3, /):
#     print(value1/value3 + value2)
#
#
# func1(1, 3, 5)
#
# # Positional or keyword with a built-in
#
# com = complex(imag=5, real=1)
# com2 = complex(real=1, imag=5)
# com3 = complex(5, 4)
# com4 = complex(10)
# print(com4)
#
#
# # defining a function with a positional or keyword
#
#
# def func2(r, i=0):
#     print(f'{r} + {i}j')
#
#
# func2(i=4, r=8)
#
# # Defining a function with keyword only
#
#
# def func3(pos1, *, live, student=' '):
#     print(live + student + str(pos1))
#
#
# func3(5, live='true')
#
#
# def some(obs, k_or_guess, my_iter='28', /, thresh='1e-05', check_finite='True', *, seed='None'):
#     print(obs+k_or_guess+my_iter+thresh+check_finite+seed)
#
#
# some('hola', 'adios', seed='some')

#
# names = ['jake', 'esteban', 'fred', 'Tim']  # List
#
# corrected_names = map(lambda name: name.title(), names)  # Iterator
#
# # print(list(corrected_names))
#
# for item in corrected_names:
#     print(item)
#
#
# for item in map(lambda x, y, z: 2*x**y-z, [1, 2, 3], [0.1, 0.2, 0.3], [1, 2]):
#     print(item)


def f(*args):
    print(args)


f(1, 2, 3, 4, 5, 6)


def my_func(*numbers):
    return numbers


a = my_func(1, 2, 3, 4,)
print(a)


def func(*numbers, **letters):
    return numbers, letters


b = func(1, 2, 3, 4, a=6, b=7)
print(b)

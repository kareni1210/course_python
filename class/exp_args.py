"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""


def sum_args(*args):
    print(sum(args))


sum_args(1, 2, 3, 4)

"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""


def concat_string(*strings):
    a = ''.join(strings)
    print(a)


concat_string('hola', 'adios')



"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""


def calculate_expenses(name, monthly_income, *expenses, **fixed_expenses):
    # print(monthly_income - sum(expenses) - sum(fixed_expenses.values()))
    for x in expenses:
        monthly_income -= x
    for y in fixed_expenses:
        monthly_income -= fixed_expenses[y]
    print(monthly_income)


calculate_expenses('Diego', 10000, 45, 100, 1500, 45,
                   internet=500, food=1000, coffe=2000)

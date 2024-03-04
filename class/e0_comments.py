"""
Excercise 0
From the file called e0_comments
Make examples of the different comments we can use in python, place
teh comment in the correct section of code
"""

a = 5  # (inline comment) this is an instance of an object, define a variable
"""
This is a block comment
we can add a lot of lines
"""

def f(x):
    """
    this is a docstring
    A docstring explains what a function does
    :param x:
    :return:
    """
    return x * x  # Return the square of x


for item in 'python':
    # An indented comment
    if item == 'p':
        # Another indented comment 
        print('Found!')

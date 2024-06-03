"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns.
The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the Internet.
"""

titles = ['Celsius', 'Farenheit']

print(f"{' | '.join(titles)}")
for _ in range(0, 101, 10):
    gf = _*1.8+31
    print(f'{_}    |   {gf}')





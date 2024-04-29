"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Equal to or over 25 but below 30 they are slightly overweight
    Equal to or over 30 but below 35 they are obese
    Equal to or over 35 they are clinically obese.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
"""
weight = float(input('What is your weight: '))
height = float(input('What is your height: '))

bmi = weight/(height**2)
print(f'Your bmi is {bmi}')

if bmi < 18.5:
    print('You are underweight')
elif 18.5 <= bmi < 25:
    print('You have a normal weight')
elif 25 <= bmi < 30:
    print('You are slightly overweight')
elif 30 <= bmi < 35:
    print('You are obese')
elif bmi >= 35:
    print('You are clinically obese')

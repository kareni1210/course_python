from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choicee = input("Make a choice (r for rock, p for paper, s for scissors: ").lower()


def uschoicee(value):
    print(" Your choice was:", end='\n')
    if value == 'r':
        return rock
    elif value == 'p':
        return paper
    elif value == 's':
        return scissors


def comchoice():
    print('The computer choice was:', end='\n')
    lista = [rock, paper, scissors]
    global a
    a = choice(lista)
    return a


if a == choicee:
    print('It is a draw')

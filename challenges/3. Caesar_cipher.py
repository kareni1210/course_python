"""
One of the first known examples of encryption was used by Julius Caesar.
Read more about here: https://en.wikipedia.org/wiki/Caesar_cipher
Create a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount, and then display the shifted message.
Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift
values so that it can be used both to encode messages and decode messages.

# When you have done the code, try to decrypt the following:
ldl ndj zcdl wdl id iwxcz ndj wpkt xbegdkts ndjg eniwdc hzxaah rdcvgpijapixdch
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = input('Enter your message: ').lower()
decision = int(input('Do you want to encrypt (0) or decrypt (1) '))
shifts = int(input('How many shifts? '))
letonum = []
n = []
mencrypt = []
mecrypt = []
lisr = []
new = []

if decision == 0:
    for _ in letters:
        num = letters.index(_)
        letonum.append(num)
    for x in letonum:
        if 0 < shifts <= 26:
            a = x+shifts
            if a < 26:
                n.append(a)
            else:
                a += - 26
                n.append(a)


print(letonum)
print(n)
print(new)

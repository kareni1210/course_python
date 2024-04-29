print('Hello, welcome to the user name generator, this program creates a username with '
      'exponential distribution (pdf and CDF), the number evaluated in the pdf and CDF'
      ' will be in your username!')
number = int(input('What is your favorite number between 0 and infinity? '))
# Es necesario poner int porque input es string
lamb = float(input('What is your favorite lambda? '))
zs = input('What is your zodiac sign? ')
pdf = lamb * pow(2.7182, -(lamb*number))
cdf = 1-pow(2.7182, -(lamb*number))
print('Your username is: ', cdf, zs, pdf, sep='')
print(f'Your username is: {cdf}{zs}{pdf}')
print('Your username: ' + str(cdf) + str(zs) + str(pdf))

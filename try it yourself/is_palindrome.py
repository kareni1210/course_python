#
# def palindromo(word):
#     tam = len(word)
#     ad = 0
#     at = -1
#     while ad <= tam-1 and at >= -tam:
#         if word[0] == word[-1]:
#             ad += 1
#             at -= 1
#         else:
#             print('La palabra NO es un palindromo :(')
#             break
#     print('La palabra SI es un palindromo :)')
#
#
# palindromo(input('Enter a word: '))


def palindrome(word):
    for _ in reversed(word):
            if x == _:
                continue
            else:
                print('La palabra no es palindrome')
                break


palindrome('oxxo')
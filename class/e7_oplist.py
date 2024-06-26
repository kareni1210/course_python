# 1. From the given list, replace the number by its name, then print out the list
numbers = [11, 4, 9, 100, 1000]
numbers[0] = 'eleven'
numbers[1] = 'four'
numbers[2] = 'nine'
numbers[3] = 'one hundred'
numbers[4] = 'one thousand'
print(numbers)

# 2. replace all numbers with the numbers 9.6 and 6 with 6 and 9.6 respectively
scores = [9.6, 6, 10, 4.5, 5, 8.2]
scores[0:2] = [6, 9.6]  # Se hace hasta el elemnto 2 porque ese ya no es tomado en cuenta
print(scores)

# 3. from the given list, there are two items that do not correspond to the list (notice the contex), delete it
items = ['red', 'purple', 'green', 'yellow', 'phone', 'magenta', 'math', 'white']
items.remove('phone')  # Delete from the original list
items.remove('math')

# del items[4]   # Once that the keyword deletes the first item it creates a new list, so you have to look at
# the new list to know the new positions, and then you can delete the next item
# del items[5]
# items.pop(4)  # Once that the method deletes the first item it creates a new list, so you have to look at
# the new list to know the new positions, and then you can delete the next item
# items.pop(5)

print(items)

# 4. delete the numbers from the list, then print out the final list
my_list = ['r', 'e', 5, 8, 'c', 'q', 9]
del my_list[2]
del my_list[2]
del my_list[-1]

# my_list.remove(5)
# my_list.remove(8)
# my_list.remove(9)

print(my_list)

# 5. insert the elements that the variables have. ANSWER: What do you observe?
a = [5, 5, 5]
b = {'key': 1}
c = ('a', 'b')
d = 'jeje'
lst = []

cont = [a, b, c, d]
lst += cont

# lst.insert(0, a)
# lst.insert(1, b)
# lst.insert(2, c)
# lst.insert(3, d)

# lst.append(a)
# lst.append(b)
# lst.append(c)
# lst.append(d)
print(lst)

# 6. Use *= as you want
s = ['Hello']
s *= 3
print(s)

# 7. Print the 1 that are in the lists
nested_list = [[[[1]]]]
print(nested_list[0][0][0][0])

# 8. Print the word
nested_list2 = [[1], [['hello']]]
print(nested_list2[1][0][0])

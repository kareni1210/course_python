# 1. With the given list, make a tuple, print out the tuple and print out some element of the tuple
list1 = [1, 2, 3]
my_tuple = tuple(list1)
print(my_tuple)

# 2. With the given list, make a tuple, print out the element with index 4 and make it upper
list2 = ['hello', 'math', 'computer', 'Dickens', 'python']
my_tuple1 = tuple(list2)
print(my_tuple1[4].upper())

# 3. Make an example using index() method with a tuple
my_tuple2 = (1, 2, 3, 4)
print(my_tuple2.index(4))

# 4. Make an example using count() method with a tuple
my_tuple3 = (1, 3, 5, 'happy', 3)
print(my_tuple3.count(3))

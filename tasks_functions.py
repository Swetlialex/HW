# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""


### YOUR CODE HERE
# def calculate_area(a,b):
#     return a*b


# ### TEST:
# print(calculate_area(10, 5))

### EXPECTED OUTPUT:
# 50


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""


### YOUR CODE HERE
# def is_even(number):
#     if number%2 == 0:
#         return True
#     else:
#         return False

# ### TEST:
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT
# True
# False


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'multiply_elements' that takes a list of integers and returns the product of all the elements in the list.
"""


### YOUR CODE HERE
# def multiply_elements(lst):
#     product = 1
#     for element in lst:
#         product = product*element
        
#     return product

# ### TEST:
# print(multiply_elements([2, 3, 4]))

### EXPECTED OUTPUT:
# 24


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function 'count_vowels' that takes a string and returns the count of vowels (a, e, i, o, u) in the string.
"""


### YOUR CODE HERE
# def count_vowels(my_str):
#     count = 0
#     vovels = 'aeiou'
#     for el in my_str:
#         if el in vovels:
#             count = count + 1
#         else:
#             continue
#     return count
    




# ### TEST:
# print(count_vowels("hello"))
# print(count_vowels("world"))

### EXPECTED OUTPUT:
# 2
# 1


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'reverse_string' that takes a string and returns the string reversed.
"""

### YOUR CODE HERE

### TEST:
# print(reverse_string("hello"))

### EXPECTED OUTPUT:
# "olleh"


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Write a function 'find_max' that takes a list of numbers and returns the largest number in the list.
"""


### YOUR CODE HERE
# def find_max(lst_number):
#     max = 0
#     for el in lst_number:
#         if el>max:
#             max = el
#     return max

# ### TEST:
# print(find_max([1, 3, 2, 8, 5]))

### EXPECTED OUTPUT:
# 8


# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
Create a function 'remove_duplicates' that takes a list and removes duplicate elements, returning a new list with unique elements.
"""


### YOUR CODE HERE
# def remove_duplicates(lst):
#     lst_unique = list(set(lst))
#     return lst_unique

# ### TEST:
# print(remove_duplicates([1, 2, 2, 3, 4, 3]))

### EXPECTED OUTPUT:
# [1, 2, 3, 4]


# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'is_palindrome' that checks if a given string is a palindrome.
"""

### YOUR CODE HERE

### TEST:
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

### EXPECTED OUTPUT:
# True
# False


# ---------------------------------- Task 9 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'add' that takes two arguments and returns their sum.
"""

### YOUR CODE HERE

### TEST:
# print(add(2, 3))

### EXPECTED OUTPUT:
# 5


# ---------------------------------- Task 10 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""


### YOUR CODE HERE
# def filter_words(lst_words, min_lenght):
#     lst_new_words = []
#     for word in lst_words:
#         if len(word) > min_lenght:
#             lst_new_words.append(word)
#     return lst_new_words



# ### TEST:
# print(filter_words(["apple", "pear", "banana", "cherry"], 5))


### EXPECTED OUTPUT:
# ['banana', 'cherry']


# ---------------------------------- Task 11 ---------------------------------- #
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""

### YOUR CODE HERE

### TEST:
#print(sorted(["cherry", "banana", "apple"], key=sort_by_last_letter))

### EXPECTED OUTPUT:
# ['banana', 'apple', 'cherry']
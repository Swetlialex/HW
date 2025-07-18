# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here
# n = int(input('Enter star numbers:'))

# for i in range(1,n+1):
#     print(i*'*')


### EXPECTED OUTPUT:
# Enter stars number: 4
# 
# **
# ***
# ****


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a script that prompts the user to enter words, one at a time.
    The user should continue to enter words until they enter '0'.
    After the user enters '0', the script should display all the words that start with a vowel (a, e, i, o, u).
"""

### Your code
# lst_words = []
# vowels=['a','e','i','o','u']

# while True:
#         word = input("Enter a word or \'0\' to stop:")
#         if word!='0':
#             for l in vowels:
#                  if word[0] == l:
#                       lst_words.append(word)
                      
#         else:
#             break
        


# print(lst_words)


### EXPECTED OUTPUT:
# Enter a word (or '0' to stop): atom
# Enter a word (or '0' to stop): see
# Enter a word (or '0' to stop): end
# Enter a word (or '0' to stop): 0
# Words that start with a vowel: ['atom', 'end']


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a script that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
words = ["hello", "world", "python", "is", "fun", "and", "useful"]

### Your code here

# result = {}                 # празен речник
# for s in words:             # взема последователно низ от списъка
#         length = len(s)     # определя дължината на низа
#         if length not in result:    # добавя дължината като ключ в речника
#             result[length] = []     # прави нов списък
#         result[length].append(s)    # добавя елемента към списъка, според броя символи в низа
# print(result)

### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['useful']}


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    In a supermarket inventory system, there are two sets of product categories:
    1. Categories that need refrigeration.
    2. Categories on sale this week.

    Write a script, which performs the following tasks:
    a. Find and print the categories that are both refrigerated and on sale.
    b. Find and print categories that are on sale but do not require refrigeration.
    c. Suggest new sale categories from the refrigerated items which are not yet on sale.

    Note: The category names are assumed to be in lowercase.
"""

### Given
refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

### Your code here
# # categories that are both refrigerated and on sale
# categories_refrigerated_and_sale =refrigerated.intersection(sale) 
# print(categories_refrigerated_and_sale)

# # categories that are on sale but do not require refrigeration
# categories_sale_not_refrigerated = sale.difference(refrigerated)
# print(categories_sale_not_refrigerated)

# # new sale categories from the refrigerated items which are not yet on sale
# categories_not_yet_on__sale_refrigerated = refrigerated.difference(sale)
# print(categories_not_yet_on__sale_refrigerated)

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}
# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a function `filter_items(input_file, filter_word)` that reads a
text file (e.g., "shopping_list.txt") and writes all lines
that contain the `filter_word` to a new file. The new file should be named
with the format `<filter_word>_items.txt`. For example, if the filter word
is "milk", the output file should be named "milk_items.txt".
"""

### Given
## shopping_list.txt content:
# 1 liter of milk
# 2 apples
# Milk chocolate
# 3 bananas


### YOUR CODE HERE

# def filter_items(input_file, filter_word):
#     # Създаваме името на изходния файл динамично
#     output_filename = f"{filter_word}_items.txt"
    

#     with open(input_file, "r") as file:
#         with open(output_filename, "w", encoding="utf-8") as output_file:
#             # Четем ред по ред
#             for line in file:
#                 # Проверяваме дали думата се съдържа в реда от файла
#                 if filter_word.lower() in line.lower():
#                     output_file.write(line)
                    
        
    
### TEST:
# filter_items("shopping_list.txt", "milk")

### EXPECTED OUTPUT:
## "milk_items.txt" with content:
# 1 liter of milk
# Milk chocolate


# ---------------------------------- Task 2 ---------------------------------- #
"""DESCRIPTION:
Write a function `remove_debug_lines(input_file, output_file)` that reads a
text file "log.txt" and removes all lines containing the word "DEBUG".
"""

### Given
## log.txt content:
# INFO - Starting process
# DEBUG - Debugging the code
# ERROR - Something went wrong
# DEBUG - Another debug message


### YOUR CODE HERE
# def remove_debug_lines(input_file, output_file):
  
    # with open(input_file, "r") as file:
    #     with open(output_file, "w", encoding="utf-8") as output_file:
    #         # Четем ред по ред
    #         for line in file:
    #             # Проверяваме дали думата DEBUG не се съдържа в реда от файла
    #             if "DEBUG" not in line.upper():
    #                 output_file.write(line)

# ### TEST:
# remove_debug_lines("log.txt", "clean_log.txt")

### EXPECTED OUTPUT:
## The file "clean_log.txt" should be:
# INFO - Starting process
# ERROR - Something went wrong


# ---------------------------------- Task 3 ---------------------------------- #
"""DESCRIPTION:
Write a function `reverse_lines(input_file, output_file)` that reverses the
content of each line in a given text file.
The reversed lines should be saved in a new file.
"""

### Given
## A text file "input.txt" with content
# Hello
# World


### YOUR CODE HERE
# def reverse_lines(input_file, output_file):
#     with open(input_file, "r") as file:
#         lines = file.readlines()  # списък от отделните редове на файла

#     with open(output_file, "w", encoding="utf-8") as out_file:    
#         for line in lines:
#         # Обръщане съдържанието на реда
#             reversed_words = ' '.join(word[::-1] for word in line.split())
#             out_file.write(reversed_words + "\n")

    

   
       
# ### TEST:
# reverse_lines("input.txt", "output.txt")

### EXPECTED OUTPUT:
## The "output.txt" with content:
# olleH
# dlroW


# ---------------------------------- Task 4 ---------------------------------- #
"""DESCRIPTION:
Write a function `remove_blank_lines(filename)` that removes all blank lines in it.
"""

### Given
## sentences.txt content:
# This is a sentence.


# Another sentence.




### YOUR CODE HERE
# def remove_blank_lines(filename):
#     with open(filename, "r") as file:
#         lines = file.readlines()

#         non_blank_lines = [line for line in lines if line.strip() != '']

#         with open(filename, 'w', encoding='utf-8') as file:
#             file.writelines(non_blank_lines)
    

        



# ### TEST:
# remove_blank_lines("sentences.txt")


### EXPECTED OUTPUT:
## The file "sentences.txt" will not contain any blank lines.
# This is a sentence.
# Another sentence.


# ---------------------------------- Task 5 ---------------------------------- #
"""DESCRIPTION:
Write a function `merge_files(file1, file2, output_file)` that merges two text
files "file1.txt" and "file2.txt" and saves the result in "merged.txt".
"""

### Given
## file1.txt content:
# Line 1 from file 1
# Line 2 from file 1

# # file2.txt content:
# Line 1 from file 2
# Line 2 from file 2


### YOUR CODE HERE
# def merge_files(file1, file2, output_file):
#     with open(file1, "r") as file:
#         lines_1 = file.readlines()  # списък от отделните редове на файл 1
#     with open(file2, "r") as file:
#         lines_2 = file.readlines()  # списък от отделните редове на файл 2

#     with open(output_file, 'w', encoding='utf-8') as file:
#         # Първи вариант
#         # for line in lines_1:
#         #     file.write(line)
#         # for line in lines_2:
#         #     file.write(line)


#         # Втори вариант
#         for line1, line2 in lines_1, lines_2:
#             file.write(line1 + line2)



# ### TEST:
# merge_files("file1.txt", "file2.txt", "merged.txt")


### EXPECTED OUTPUT:
# The file "merged.txt" with content:
# Line 1 from file 1
# Line 2 from file 1
# Line 1 from file 2
# Line 2 from file 2


# ---------------------------------- Task 6 ---------------------------------- #
"""DESCRIPTION:
Write a function `backup_files(src, dest)` that copies all files (but not directories)
from the source folder "src" to the destination folder "dest".

For each file, attach a timestamp suffix with current date and time to the filename
in the format 'YYYY-MM-DD_HH-MM-SS'.
For example: /src/track1.mp3 => /dest/track1.mp3_2020-01-01_18-30-45

If the destination folder doesn't exist, create it.
Do not remove the files from the source folder.

"""

### Given
# Source folder "src" contains the following files:
# /src/track1.mp3
# /src/track2.mp3
# /src/photo.jpg

# Destination folder "dest" may or may not exist.

### YOUR CODE HERE

# import os
# import shutil
# from datetime import datetime

# def backup_files(src, dest):
#     # Създава папката за архив, ако не съществува
#     os.makedirs(dest, exist_ok=True)

#     # Взима текущия момент във формат 'ГГГГ-ММ-ДД_ЧЧ-ММ-СС'
#     timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

#     # Обхожда всички елементи в изходната папка
#     for item in os.listdir(src):
#         src_path = os.path.join(src, item)

#         # Проверява дали е файл (а не директория)
#         if os.path.isfile(src_path):
#             # Създава ново име на файла с добавен времеви печат
#             new_filename = f"{item}_{timestamp}"
#             dest_path = os.path.join(dest, new_filename)

#             # Копира файла в целевата папка с новото име
#             shutil.copy2(src_path, dest_path)

# ### TEST:
# backup_files("src", "dest")

### EXPECTED OUTPUT:
## If the program is executed at 26.03.2025, 15:45:00 the "dest" folder sould contain:
# /dest/track1.mp3_2025-03-26_15-45-00
# /dest/track2.mp3_2025-03-26_15-45-00
# /dest/photo.jpg_2025-03-26_15-45-00

# The original files in the "src" folder remain untouched. If "dest" folder
# doesn't exist, it will be created automatically.
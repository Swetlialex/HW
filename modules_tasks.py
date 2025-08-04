# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a custom module named 'custom_math'.
Inside this module, define two functions: one that calculates the area of a circle (given the radius) and another that calculates the area of a square (given the side length).
Then, write a script that imports this module and uses these functions.
"""

# ### Your script to use custom_math
# # main.py

# from custom_math import area_circle, area_square

# # Въвеждане на стойности
# radius = float(input("Enter the radius of the circle: "))
# side = float(input("Enter the side length of the square: "))

# # Изчисления
# circle_area = area_circle(radius)
# square_area = area_square(side)


# ### Test:

# print(f"The area of the circle is: {circle_area:.2f}")
# print(f"The area of the square is: {square_area:.2f}")


### EXPECTED OUTPUT:
# Enter the radius of the circle: 5
# Enter the side length of the square: 4
# The area of the circle is: 78.5375
# The area of the square is: 16

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a package named 'data_processing'. Inside this package, create two modules: 'loader' and 'analyzer'.
In 'loader', define a function that returns a hardcoded list of values ([10, 20, 30, 40, 50]).
In 'analyzer', define a function that calculates the average of the data.
Finally, write a script that uses this package to load data and compute its average.
"""

### Your script to use data_processing package
# main.py

# from data_processing import loader
# from data_processing import analyzer

# # Test:
# data = loader.load_data()
# average = analyzer.calculate_average(data)
# print(f"The average is: {average}")

### EXPECTED OUTPUT:
# The average is: 30.0

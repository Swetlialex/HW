# # Създаваме собствен декоратор
# def shout(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# # shout „опакова“ функцията greet, така че върнатият текст да е с главни букви.
# @shout
# def greet():
#     return "Здравей, Светла!"
# # @shout е същото като greet = shout(greet)
# # greet = shout(greet)
# print(greet())  # → ЗДРАВЕЙ, СВЕТЛА!


# # decorator
# def stars_decorator(f):
#     def wrapper():
#         print("*" * 50)
#         f()
#         print("*" * 50)

#     return wrapper

# @stars_decorator
# def greet():
#     print("Howdy World!")

# # let's decorate greet:
# # greet = stars_decorator(greet)

# # and use it:
# greet()


# # decorator
# def stars_decorator(f):
#     def wrapper(n):
#         print("*" * 50)
#         f(n)
#         print("*" * 50)

#     return wrapper

# def greet(name):
#     print("Howdy {}!".format(name))

# # let's decorate greet:
# greet = stars_decorator(greet)

# # and use it:
# greet("Pesho")


# Декоратор, който приема произволен брой аргументи
def stars_decorator(f):
    def wrapper(*args, **kwargs):
        # *args улавя всички позиционни аргументи - име, фамилия,а **kwargs всички именовани аргументи - в двойки, като за речник: language="Bulgarian"
        print("*" * 50)
        f(*args, **kwargs)
        print("*" * 50)
    return wrapper

# декорираме функцията greet
@stars_decorator
def greet(name, greeting="Howdy"):
    print(f"{greeting} {name}!")

greet("Светла")
greet("Петър", greeting="Здравей")

# Пример с върната стойност

def log_decorator(f):

  def wrapper(a,b):
    print("LOG: The function was executed!")
    return f(a,b)

  return wrapper

@log_decorator
def sum(x,y):
  return (x+y)


print( sum(2,3) )



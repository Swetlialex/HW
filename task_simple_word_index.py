
text = """apple and banana one apple one banana
          a red apple and a green apple"""

my_list = text.split()
print(my_list)
for num in set(my_list):
    print(f"{num:<10}-{my_list.count(num):>3}")





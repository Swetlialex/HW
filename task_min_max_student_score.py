student_score = {
                'Ivan'  :5.00,
                'Alex'  :3.50,
                'Maria' :5.50,
                'Georgy':5.00
                }
# преобразувам ключовете в списък и стойностите в списък
for key, value in student_score.items():
    lst_key = list(student_score.keys())
    lst_value = list(student_score.values())

# print(lst_key)
# print(lst_value)

# намирам максималната и минималната стойности в списъка със стойности
max_value = max(lst_value)
# print(max_value)
min_value = min(lst_value)
# print(min_value)

# отпечатвам max              
for key, value in student_score.items():
    if value == max_value:
        print(f'{key} - {value}')
        
# отпечатвам min  
for key, value in student_score.items():
    if value ==min_value:
        print(f'{key} - {value}')



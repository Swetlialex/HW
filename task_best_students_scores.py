student_score = {
                'Ivan'  :5.00,
                'Alex'  :3.50,
                'Maria' :5.50,
                'Georgy':5.00
                }
# print(student_score)

for key,value in student_score.items():
    if value >=5.0:
      print(f'{key:<15} - {value:>5.2f}')



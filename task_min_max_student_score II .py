# ВТОРИ ВАРИАНТ НА РЕШЕНИЕ - ПО-РАЦИОНАЛЕН
student_score = {
                'Ivan'  :5.00,
                'Alex'  :3.50,
                'Maria' :5.50,
                'Georgy':5.00
                }

print(max(student_score, key=student_score.get), '-', max(student_score.values()))
print(min(student_score, key=student_score.get), '-', min(student_score.values()))

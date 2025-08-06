# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a function (format_current_date) that returns the current date and time in the format "YYYY-MM-DD HH:MM:SS".
"""

### YOUR CODE HERE:
# from datetime import datetime

# def format_current_date():
#     current_datetime = datetime.now()
#     return current_datetime
# ### TEST:
# print(format_current_date())

### EXPECTED OUTPUT:
# Output will vary depending on when the function is called. Example: "2024-02-11 22:34:56"


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a function (days_between) that calculates the number of days between two dates given in the format "YYYY-MM-DD".
"""

### YOUR CODE HERE:
# from datetime import datetime, timedelta

# def days_between(date1, date2):
#     d1 = datetime.strptime(date1, "%Y-%m-%d")
#     d2 = datetime.strptime(date2, "%Y-%m-%d")
#     return abs((d2 - d1).days)

    
# ### TEST:
# print(days_between("2024-01-01", "2024-02-01"))

### EXPECTED OUTPUT:
# 31


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function (get_weekday) that takes a date in the format "YYYY-MM-DD" and returns the name of the day of the week.
"""

### YOUR CODE HERE:
# from datetime import datetime

# def get_weekday(date_str):
#     # Преобразуваме низa в дата
#     date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
#     # Списък с дни от седмицата на български
#     days_bg = ["Понеделник", "Вторник", "Сряда", "Четвъртък", "Петък", "Събота", "Неделя"]
    
#     # Вземаме индекса на деня и връщаме съответния
#     return days_bg[date_obj.weekday()]


# ### TEST:
# print(get_weekday("2024-02-11"))

### EXPECTED OUTPUT:
# "Sunday"




# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Write a function (calc_days_untill_birthdate), that calculates the remaining days from current date to your next birthday day.
"""

### YOUR CODE HERE:
# from datetime import datetime, timedelta

# def calc_days_until_birthdate(birthdate_str):
   
#     current_date = datetime.now().date()
#     birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y")

# # Създаваме дата за рожден ден тази година
#     next_birthday = datetime(day=birthdate.day, month=birthdate.month, year=current_date.year).date()

# # Ако вече е минал рожденият ден тази година
#     if next_birthday < current_date:
#         next_birthday = datetime(day=birthdate.day, month=birthdate.month, year=current_date.year + 1).date()

# # Изчисляваме разликата
#     delta = next_birthday - current_date
#     return delta.days

# ### TEST:
# birthdate = "25.02.1990" # 25th February 1990
# print(f"Days until next birthday: {calc_days_until_birthdate(birthdate)}")


### EXPECTED OUTPUT:
# if today date is "15.02.2024", the output should be:
# Days until next birthday: 9
# функцията валидира името 
def validation_name(): 
    while True:
        user_name = input('Въведете Вашето име:')
        if len(user_name) <= 2:
            print('Некоректни данни! Въведи име с повече от 2 символа: ')
            
        else: break
    return user_name

# функцията валидира теглото в килограми в диапазона [5;300]
def validation_weight():
    while True:
        user_weight = float(input("Тегло в килограми:")) #тегло в килограми 
        if user_weight<5 or user_weight>300:
            print('Некоректни данни! Въведи тегло в диапазона [5;300]: ')
            
        else: break
    return user_weight

# функцията валидира ръста в сантиметри в диапазона [50;300]
def validation_height():
    while True:
        user_height = float(input("Височина в сантиметри: ")) # височина в сантиметри
        if user_height<50 or user_height>250:
            print('Некоректни данни! Въведи ръст в диапазона [50;250]: ')
            
        else: 
            break
    return user_height

# главна функция 
def get_user_data():
    """събира трите функции в един вход на данни"""
    user_data = {}

    user_data['name'] = validation_name()
    user_data['height'] = validation_height()
    user_data['weight'] = validation_weight()
    print(f'Вие сте {user_data['name']} с тегло от {user_data['weight']} кг и ръст от {user_data['height']} см.' )
    return user_data

    """Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user heigth in centimeters",
                "weight": "user weight in kilograms"
            }
    """


# извикваме главната функция за изпълнение
get_user_data()
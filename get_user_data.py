
def get_user_data():
    """retrieves user data from the command line"""
    user_data = {}

    
    while True:
        user_name = input('Въведете Вашето име:')
        if len(user_name) <= 2:
            print('Некоректни данни! Въведи име с повече от 2 символа: ')
            user_name = input('Вашето име: ')
        else: break

    
    while True:
        user_weight = float(input("Тегло в килограми:")) #тегло в килограми 
        if user_weight<5 or user_weight>300:
            print('Некоректни данни! Въведи тегло в диапазона [5;300]: ')
            user_weight = float(input('Вашето тегло: '))
        else: break

    
    while True:
        user_height = float(input("Височина в сантиметри: ")) # височина в сантиметри
        if user_height<50 or user_height>250:
            print('Некоректни данни! Въведи ръст в диапазона [50;250]: ')
            user_height = float(input('Вашият ръст: '))
        else: 
            break

    user_data['name'] = user_name
    user_data['height'] = user_height
    user_data['weight'] = user_weight
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



get_user_data()
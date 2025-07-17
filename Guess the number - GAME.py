import random
number = random.randint(1,10)
print(number)
counter_guess = 0
user_number = int(input("Play \'Guess number\'! You are entitled to 5 attempts. Enter a number from 1 to 10:"))

if user_number > 10 or user_number < 1:
    print("Your guess is out of bounds.")

else:

    while True:

        if user_number == number:
            counter_guess +=1
            print(f"Bravo, you guessed my number. The number is {number} and the guess counter is {counter_guess}")
            break
        else:
            if user_number < number:
                counter_guess +=1
                if counter_guess <5:
                    print("Too low!")
                    user_number = int(input("Try again:"))
                else: 
                    print('You lost! Please, restart game!')
                    break
            else:
                counter_guess +=1
                if counter_guess <5:
                    
                    print("Too hight!")
                    user_number = int(input("Try again:"))
                else:
                    print('You lost! Please, restart game!')
                    break



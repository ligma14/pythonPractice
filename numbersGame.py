import random
# TODO: Можно добавить счетчик за сколько попыток человек угадал число
# Еще можно сделать таблицу с рекордами

def numbersGame():
    # Generate a random number between 1 and 1000
    target_number = random.randint(1, 1000)
    previous_guess = None
    i = 0 # Counts the number of guesses the user made
    
    print("Добро пожаловать в numbersGame")
    print("Правила игры: Вам предстоит угадать число от 1 до 1000")
    
    while True:
        try:
            # Get user's guess
            guess = int(input("Введите число: "))
            
            if guess < 1 or guess > 1000:
                print("Пожалуйста введите число от 1 до 1000")
                continue
            
            # Check if the guess is correct
            if guess == target_number:
                print(f'Поздравляем, Вы успешно угадали число за {i} попыток!')
                break
            
            # Provide feedback on how close the guess is
            if previous_guess is not None:
                if abs(target_number - guess) < abs(target_number - previous_guess):
                    i += 1
                    print(f"Горячее! Попытка номер {i}")
                else:
                    i += 1
                    print(f"Холоднее! Попытка номер {i}")
            
            # Update the previous guess
            previous_guess = guess
        
        except ValueError:
            print("Ошибка: Убедитесь что вы вводите число")
    
    print("Спасибо за игру!")

# Run the game
numbersGame()

import random
import json
import os

RECORDS_FILE = "numbersGame_records.json"   

# LOAD_RECORDS()
def load_records():
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, "r") as file:
            return json.load(file)
    return []

# SAVE_RECORDS()
def save_record(record):
    records = load_records()
    records.append(record)
    with open(RECORDS_FILE, "w") as file:
        json.dump(records, file, indent=4)

# DISPLAY_RECORDS()
def display_records():
    records = load_records()
    if records:
        print("\nВаши рекорды:")
        for record in records:
            print(f"Player: {record['player']}, Попытки: {record['guesses']}")
    else:
        print("\nПредыдущие рекорды не найдены.")

# GAME_CODE
def numbersGame():
    # Generate a random number between 1 and 1000
    target_number = random.randint(1, 1000)
    previous_guess = None
    guess_count = 0 # Counts the number of guesses the user made
    
    print("Добро пожаловать в numbersGame")
    print("Правила игры: Вам предстоит угадать число от 1 до 1000")

    player_name = input("Пожалуйста, введите ваше имя:")
    
    while True:
        try:
            # Get user's guess
            guess = int(input("Введите число: "))
            
            if guess < 1 or guess > 1000:
                print("Пожалуйста введите число от 1 до 1000")
                continue
            
            # Check if the guess is correct
            if guess == target_number:
                print(f'Поздравляем, {player_name}, Вы успешно угадали число за {guess_count} попыток!')
                save_record({"player": player_name, "guesses": guess_count})
                break
            
            # Provide feedback on how close the guess is
            if previous_guess is not None:
                if abs(target_number - guess) < abs(target_number - previous_guess):
                    guess_count += 1
                    print(f"Горячее! Попытка номер {guess_count}")
                else:
                    guess_count += 1
                    print(f"Холоднее! Попытка номер {guess_count}")
            
            # Update the previous guess
            previous_guess = guess
        
        except ValueError:
            print("Ошибка: Убедитесь что вы вводите число")
    
    display_records()
    print("Спасибо за игру!")

# Run the game
numbersGame()

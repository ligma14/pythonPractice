import random
import string

def generate_random_password():
    print("Добро пожаловать в passwordGenerator")
    print("Правила: Вам необходимо ввести количество символов для генерируемого пароля. Пароль создается из набора случайных символов, чисел и букв")

    while True:
        try:
            # Get user's input
            length = int(input("Введите число символов для генерации пароля: "))

            if length > 16:
                print("Ты точно думаешь что тебе нужен пароль свыше 16 символов? Подумай еще раз.")
                continue

            if length < 4:
                print("Ты думаешь пароль в несколько символов защитит тебя? Подумай еще раз.")
                continue

            else: 
                # Define the character set: letters, digits, and symbols
                characters = string.ascii_letters + string.digits + string.punctuation
                print("Генерируем случайный пароль..")
                # Generate a random password
                password = ''.join(random.choice(characters) for _ in range(length))
                return password    
            
        except:
            print('Ошибка: убедитесь что вводите число')


# Generate a random password
password = generate_random_password()
print(f"Ваш случайный пароль: {password}")
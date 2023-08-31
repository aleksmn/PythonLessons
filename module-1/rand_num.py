import random

number = random.randint(0, 5)

print("Попробуй угадать число от 0 до 5!")

attempts = 3
user_number = ''

while user_number != number and attempts > 0:
    user_number = int(input("Введи число: "))
    attempts -= 1    

if user_number == number:
    print("Это верно, я загадал число", number)
    print("Ты выиграл")
else:
    print("Ты проиграл")
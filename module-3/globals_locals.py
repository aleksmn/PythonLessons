# Пространства имен


# Глобальная переменная
username = "Vasya99"
color = "Красный"

def get_user():
    # глобальная внутри функции
    global color
    color = "Зеленый"

    # локальная переменная
    username = "Dima123"
    print("Имя:", username)


# Вызываем функцию
get_user()
print(username)
print(color)


# Локальные и глобальные переменные

# Глобальная переменная
username = "User"
color = "purple"


def get_user():

    # глобальная переменная внутри функции
    global color
    color = "red"

    # Локальная переменная
    username = "Дмитрий"


    print("Имя пользователя", username)
    print("Любимый цвет", color)

    print("Локальное пространство имен",locals())
    print("Глобальное пространство имен", globals())




# Вызываем функцию    
get_user()

print(username)
print(color)

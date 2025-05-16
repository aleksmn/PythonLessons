def my_decorator(func):
    def wrapper():
        print("Что-то делаем перед функцией...")
        func()
        print("Что-то делаем после функции...")

    return wrapper


@my_decorator
def hello():
    print("Hello!")


hello()


# Декорированная функция
# decorated_hello = my_decorator(hello)

# decorated_hello()

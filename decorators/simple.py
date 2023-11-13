def my_decorator(func):
    def wrapper():
        print("Что-то делаем перед функцией...")
        func()
        print("Что-то делаем после функции...")

    return wrapper

def hello():
    print("Hello!")


hello = my_decorator(hello)

hello()

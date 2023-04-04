
# Необязательный аргумент
def say_hello(name: str = 'Пользователь'):
    return "Привет " + name + "!"



print(say_hello("Дима"))
print(say_hello())



def get_sum(*args):

    result = 0

    for num in args:
        result += num

    return result


print(get_sum(2, 6, 1, 8, 9))


def create_user(**params):
    
    return(params)


print(create_user(fname="Виталий", lname="Иванов", job='Учитель'))



# До / можно записывать только позиционные аргументы

def diff(num1, num2, /):
    return num1 - num2


print(diff(3, 5))









# Написать функцию, которая принимает число
# и выводит таблицу умножения для этого числа

def multiplication_table(num):
    num = 5
    for j in range(1, 11):
        print(f"{num} * {j} = {num*j}")




multiplication_table(5)
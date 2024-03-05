import random


def get_random_list(start, end, length):
    rand_list = [] # список случайных чисел

    for i in range(length):
        rand_num = random.randint(start, end)
        rand_list.append(rand_num)

    # Возвращаем список
    return rand_list



print(get_random_list(1, 100, 5))
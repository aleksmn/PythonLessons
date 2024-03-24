def add_num():
    nums_list = []

    while True:
        n = input("Введите число: ")
        # Условие выхода из цикла
        if n == "":
            print("Ввод чисел закончен")
            break
        else:
            # добавляем число в список
            nums_list.append(int(n))
            

    # Возвращаем список
    return nums_list



def check(nums):
    for n in nums:
        if n > 10:
            # Выходим из функции
            #  и возвращаем False
            return False
    # если нет чисел больше 10, то возвращаем True
    return True


# Проверки
my_list = add_num()
print(my_list)


print(check(my_list))
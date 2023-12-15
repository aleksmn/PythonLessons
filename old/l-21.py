
def greet_people(*args):
    for name in args:
        print("Привет " + name + "!")


greet_people("Андрей", "Николай", "Мария", "Юлия", "Олег")


















def convertTemp(temp, scale):

    if scale == 'f':
        return (temp - 32) / 1.8

    if scale == 'c':
        return temp * 1.8 + 32

    return "Неверный ввод"





# print(convertTemp(32, 'f'))

# print(convertTemp(0, 'c'))

# print(convertTemp(' ', ' '))



# def convertTemp(temp, scale="c"):
#     # print("Переводим температуру", temp)
#     # print("из шкалы", scale)

#     if scale == "c":
#         new_temp = temp * 1.8 + 32
#     elif scale == "f":
#         new_temp = (temp - 32) / 1.8
#     else:
#         new_temp = None

#     return new_temp


# print(convertTemp(0, "f"))

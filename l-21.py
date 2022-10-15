

# def greet_people(*args):
#     for name in args:
#         print("Привет " + name + "!")


# greet_people("Андрей", "Николай", "Мария", "Юлия")


# def convertTemp(temp, scale):

#     if scale == 'f':
#         res = (temp - 32) / 1.8
#     elif scale == 'c':
#         res = temp * 1.8 + 32

#     print(res)


# convertTemp(32, 'f')
# convertTemp(0, 'c')


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

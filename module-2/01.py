# items = []
# temp = []
# while True:
#     temp = [input('Товар: \n')]
#     if temp == ['']:
#         break
#     else:
#         items.append(*temp)
# print(items)


# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
# while True:
#     a = input('Индекс: \n')
#     if a == '':
#         break
#     else:
#         try:
#             deals.pop(int(a))
#         except:
#             pass
# print(deals)




months = [
'январь', 'февраль', 'март', 'апрель',
'май', 'июнь', 'июль', 'август',
'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
]

# Напиши решение ниже:
winter = [months[-1], months[0], months[1]]
spring = months[2:5]
summer = months[5:8]
autumn = months[8:11]


print('Зима:', winter)
print('Весна:', spring)
print('Лето:', summer)
print('Осень:', autumn)
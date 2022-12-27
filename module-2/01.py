# items = []
# temp = []
# while True:
#     temp = [input('Товар: \n')]
#     if temp == ['']:
#         break
#     else:
#         items.append(*temp)
# print(items)


deals = [
    'погулять с друзьями',
    'почитать новости и сцепиться с кем-нибудь в комментах',
    'почитать книжку',
    'рассмотреть потолок',
    'поиграть в Brawl stars',
    'помыть посуду',
    'сказать родителям, что заболел',
    'залипнуть в летсплеях по роблоксу',
]
while True:
    a = input('Индекс: \n')
    if a == '':
        break
    else:
        try:
            deals.pop(int(a))
        except:
            pass
print(deals)

months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
          'Декабрь')

winter = months[-1:] + months[0:2]
spring = months[2:5]
summer = months[5:8]
autumn = months[8:11]


print(winter[0], winter[1], winter[2])

# Распаковка списка или кортежа
print(*winter)


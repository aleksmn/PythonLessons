"""
Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, 
после чего дробная часть копеек отбрасывается. Определите, через сколько лет 
вклад составит не менее Y рублей. 
"""


# x = float(input('Введите сумму вклада: '))
# p = float(input('Введите процент: '))
# y = float(input('Введите сумму цели: '))
# i = 0
# while x < y:
#     x *= 1 + p / 100
#     x = int(100 * x) / 100

#     print(f'Сумма: {x}')

#     i += 1
# print('Понадобится ', i)




"""
Банк принимает от посетителя начальную сумму вклада в рублях 
на несколько лет под определенный годовой процент. Условия таковы, 
что в каждом последующем году процент вычисляется не от начальной 
суммы вклада, а от общей с учетом суммы процентов (дохода) 
за прошедший период.

"""



C = float(input("Введите начальную сумму вклада"))
n = int(input("На сколько лет?"))
p = float(input("Под какой процент?"))
#------------------
S = C
for i in range(0,n):
    S = S / 100.0 * p + S       # итерация с увеличением исходной суммы
print ('Количество денег за', n, 'лет составит', S, 'рублей')
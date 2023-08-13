'''
Задача 1. Что выведет программа?
st1 = '12'
st2 = '34'
x1 = int(st1)
x2 = int(st2)
print(x1, '-',  x2, ' =',  x1 – x2)   
st1 = st1 * 2
st2 = 4 * st2
print(st1 + '+' + st2 + '=' + st1 + st2)
st3 = st2 + st1
print('st3 =' + st3)
x3 = int(st1) + int(st2)
print(int(st1), '+', int(st2), ' =', x3)

Задача 2. Что выведет программа?
st = '98765+йцукен+12345'
print(len(st))
print(st[0] + st[-1])
print(3*st[4] + 4*st[7])
print(3*int(st[4]) + 4*int(st[15]))

Задача 3. Что выведет программа?
st = 'abz1sd2dv3fk4gm5qn6xw7e'
for i in range(len(st)):
    if i % 3 == 0:
        print(st[i], end = '')

Задача 4. Что выведет программа?
st = '123456789'
print(st[len(st) -2] + st[len(st) -2])
print(int(st[len(st) -2]) + int(st[len(st) -2]))
print(st[len(st)])
'''
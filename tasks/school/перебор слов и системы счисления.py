'''
Шифр кодового замка представляет собой последовательность из пяти символов, 
каждый из которых является цифрой от 1 до 4. Сколько различных вариантов шифра 
можно задать, если известно, что цифра 1 встречается ровно два раза, а каждая 
из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

'''


from itertools import product

alphabet = '1234'
ap=[]
for i in product(alphabet, repeat=5):    
    if i.count('1') == 2:
        ap.append(i)

print(len(ap))



'''
Сколько существует различных трёхзначных чисел, 
записанных в четверичной системе счисления, 
в записи которых сумма первой и последней цифры строго больше цифры стоящей по середине?

'''

from itertools import product 
alphabet = '0123'
ap=[]
for i in product(alphabet, repeat=3):    
    if (i[0] != '0') and (int(i[0]) + int(i[2]) > int(i[1])):
        ap.append(i)
print(len(ap))
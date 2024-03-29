''''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.

1)Строится двоичная запись числа N.
2)К этой записи дописываются справа ещё два разряда по следующему правилу:
а)складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись 111001;
б)над этой записью производятся те же действия — справа дописывается остаток от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.

Укажите минимальное число R, которое превышает 43 и может являться результатом работы алгоритма. В ответе это число запишите в десятичной системе.
'''
for n in range(100):
    s = bin(n)[2:]
    k = s.count('1')
    s = s + str(k % 2)
    k = s.count('1')
    s = s + str(k % 2)
    r = int(s,2)
    if r > 43:
        print(r)
        break




'''

Автомат обрабатывает натуральное число N (128 ≤ N ≤ 255) по следующему алгоритму:

1.Строится восьмибитная двоичная запись числа N.
2.Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
3.Полученное число переводится в десятичную запись.
4.Из исходного числа вычитается полученное, разность выводится на экран.

Пример. Дано число N = 131. Алгоритм работает следующим образом:

1.Восьмибитная двоичная запись числа N: 10000011.
2.Все цифры заменяются на противоположные, новая запись: 01111100.
3.Десятичное значение полученного числа: 124.
4.На экран выводится число: 131 – 124 = 7.

Какое число нужно ввести в автомат, чтобы в результате получилось 105?


'''


for n in range(128, 256):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2)  # перевод в десятичную систему
    if n - r == 105:
        print(n)



'''
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:

1. Строится двоичная запись числа N.
2. Вместо последней (самой правой) двоичной цифры дважды записывается вторая слева цифра двоичной записи.
3. Результат переводится в десятичную систему.

Пример. Дано число N = 19. Алгоритм работает следующим образом:

1. Двоичная запись числа N: 10011.
2. Вторая слева цифра 0, единица в конце записи заменяется на два нуля, новая запись 100100.
3. Результат работы алгоритма R = 36.

При каком наименьшем числе N в результате работы алгоритма получится R > 92? В ответе запишите это число в десятичной системе счисления.


'''

for n in range(4, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    s = s[0:-1]
    s += s[1] * 2
    r = int(s, 2)  # перевод в десятичную систему
    if r > 92:
        print(n)
        break
'''
1. Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. 
Строки содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, 
в которых буква E встречается чаще, чем буква A.


2. Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
Определите символ, который чаще всего встречается в файле сразу после буквы A.

Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу 
— A и D. Для этого текста ответом будет B.

'''



f = open('string_2.txt')
a = 0
for string in f:
    if(string.count('A') < string.count('E')):
        a += 1
print(a)



f = open('string_2.txt').readline()
j=''
for i in range(len(f)-1):
    if f[i] == 'A':
        j += f[i+1]
print(max(set(j),key = j.count))



s = f.readline()
a = [0] * 26
maxi = 0
for i in range(len(s) - 1):
    if s[i] == 'A':
        a[ord(s[i + 1]) - 65] += 1
for i in range(26):
    if a[i] > maxi:
        maxi = a[i]
        index = i
print(chr(index + 65))
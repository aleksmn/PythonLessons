'''
Напишите программу для решения арифметического ребуса
       КТО + КОТ = ТОК 
 где различные буквы надо заменить на различные цифры.
 Найдите одно первое решение. Выведите его на экран. Также выведите
 количество проходов, которое выполнила ваша программа.
 
 Замечание 1: можно сначала попробовать написать программу с вложенными
 циклами for, а потом модифицировать её в программу с вложенными
 циклами while.

 Замечание 2: используйте целочисленную арифметику (НЕ СТРОКИ).
'''



# FOR

kp = 0 # счётчик количества проходов
for k in range(1, 10): 
                       
    for t in range(1, 10): 
        for o in range(0, 10): 
            kp += 1
            kto = k * 100 + t * 10 + o
            kot = k * 100 + o * 10 + t
            tok = t * 100 + o * 10 + k
            if k != t != o != k and kto + kot == tok:
                print('Решение ребуса:  ', kto, '+', kot, '=', tok)
                kp_rebus = kp 

print('Количество проходов ДО того, как цифры нашли:', kp_rebus)
print('Количество ВСЕХ проходов:', kp)    





# WHILE

flag = False # пока цифры для букв не найдены
kp = 0 # счётчик количества проходов
k = 1
while k < 10 and not flag:
    t = 1 
    while t < 10 and not flag: 
        o = 0 
        while o < 10 and not flag: 
            kp += 1 #счетчик проходов
            
            kto = k * 100 + t * 10 + o
            kot = k * 100 + o * 10 + t
            tok = t * 100 + o * 10 + k
            # Проверяем условие (во внутреннем цикле)
            if k != t != o != k and kto + kot == tok:
                flag = True
                kp_rebus = kp
            o += 1 
        t += 1     
    k += 1 
# Вывод ответа после цикла:
print('Решение ребуса:  ', kto, '+', kot, '=', tok)
print('Количество проходов ДО того, как цифры нашли:', kp_rebus)
print('Количество всех проходов:', kp)  

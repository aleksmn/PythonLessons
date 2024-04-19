'''
1. Текстовый файл состоит не более чем из 10^6 символов арабских цифр (0, 1, ..., 9). 
Определите максимальное количество идущих подряд цифр, расположенных в строгом убывающем порядке.

2. Текстовый файл состоит не более чем из 10^6 символов арабских цифр (0, 1, ..., 9).
  Определите максимальное количество идущих подряд цифр, среди которых каждые две соседние различны.


3. Текстовый файл состоит не более чем из 10^6 символов арабских цифр (0, 1, ..., 9).
 Определите максимальное количество идущих подряд цифр, среди которых сумма двух идущих 
 подряд чисел больше числа следующего за ними.

'''
# 1

f=open('string_3.txt').readline()
maxi=count=1
for i in range(1,len(f)):
    if f[i-1] > f[i]:
        count+=1
    else:
        maxi=max(count,maxi)
        count=1
print(maxi)



# 2

f=open('string_3.txt').readline()
maxi=count=1
for i in range(1,len(f)):
    if f[i-1] != f[i]:
        count+=1
    else:
        maxi=max(count,maxi)
        count=1
print(maxi)


# 3
f=open('string_3.txt').readline()
count = 0
maxi = 0
for i in range(2,len(f)):
    if int(f[i-2]) + int(f[i - 1]) > int(f[i]):
        count += 1
    else:
        count += 2
        if (count > maxi):
            maxi = count
        count = 0
print(maxi)
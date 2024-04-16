'''
1. Текстовый файл состоит не более чем из 10^6 символов X, Y и Z. 
Определите максимальное количество идущих подряд символов, 
среди которых каждые два соседних различны.



2. Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности, 
состоящей из символов X. Хотя бы один символ X находится в последовательности.


3. Текстовый файл состоит не более чем из 106 символов X, Y и Z. 
Определите максимальную длину цепочки вида XYZXYZXYZ... 
(составленной из фрагментов XYZ, последний фрагмент может быть неполным).

'''




#  1
f = open("string_1.txt").readline()

# XXYXXXZXXZXYXXXXYYYXXXXYYYXXXYYXYZYXYYXYXXX

counter = 1
max_counter = 0

for i in range(1, len(f)):
    # print(f[i], f[i-1])
    if f[i] != f[i-1]:
        counter += 1
    else:
        if counter > max_counter:
             max_counter = counter
        
        counter = 1

print(max_counter)


#  2
f = open("string_1.txt").readline()


counter = 1
max_counter = 0

for i in range(1, len(f)):
    # print(f[i], f[i-1])
    if f[i] == f[i-1] == "X":
        counter += 1
    else:
        if counter > max_counter:
             max_counter = counter
        
        counter = 1

print(max_counter)



# 3
k = m = 0
for i in range(len(f)):
    if (f[i] == 'X' and k%3 == 0) or (f[i] == 'Y' and k%3 == 1) or (f[i] == 'Z' and k%3 == 2):
        k += 1
        m = max(m, k)
    elif f[i] == 'X': k = 1
    else: k = 0
print(m)

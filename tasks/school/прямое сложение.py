"""
Значение арифметического выражения: 9**8 + 3**5 - 9
записали в системе счисления с основанием 3. 
Сколько цифр «2» содержится в этой записи?

"""


# Перевести в троичную систему
x = 9

result = ""

while x != 0:
    # print(x % 3)
    result += str(x % 3)
    x = x // 3
    
    # print(x)

result = result[::-1]
print(result)
print(result.count("2"))
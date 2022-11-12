# Напиши функцию, которая будет принимать аргументом цепочку ДНК 
# и проверять её правильность. Если в цепочке встречаются какие-то 
# символы помимо A, T, C и G, функция должна возвращать False, 
# а если цепочка правильная, то True. Функция должна быть чистой 
# и использовать подсказки типов.




dna = "ATCG"
input_dna = input("Введите ДНК ")


def check_dna(dna_for_test: str):
    for s in input_dna.upper():
        if s in dna:
            return False
        
    return True


print(check_dna(input_dna))


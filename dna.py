def DNA_reverse(dna: str):
    new_dna = ""
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    for key in dna:
        new_dna += pairs[key]

    return new_dna


test1 = "ATCG"
test2 = "ACTAGCGTCAGCTAGCTCGGTCAATTCGCTATGCGATCGCGCTTTAAC"

print(DNA_reverse(test1))
print(DNA_reverse(test2))


# Напиши функцию, которая будет принимать аргументом цепочку ДНК
# и проверять её правильность. Если в цепочке встречаются какие-то
# символы помимо A, T, C и G, функция должна возвращать False,
# а если цепочка правильная, то True. Функция должна быть чистой
# и использовать подсказки типов.


# dna = "ATCG"
# input_dna = input("Введите ДНК ")


# def check_dna(dna_for_test: str):
#     for s in input_dna.upper():
#         if s not in dna:
#             return False

#     return True


# print(check_dna(input_dna))

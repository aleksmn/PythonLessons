# Цепочка ДНК состоит из двух рядов нуклеотидов, соединённых вместе. 
# Интересно, что нуклеотид A может соединяться только с нуклеотидом T, C с G 
# и наоборот. Получается, зная содержимое одной стороны цепочки ДНК, 
# всегда можно воссоздать и вторую.

# Напиши функцию, которая принимает аргументом цепочку ДНК в виде строки 
# и возвращает её пару.


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

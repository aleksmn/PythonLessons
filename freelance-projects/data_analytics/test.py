# test_dict = {
#     'x': 4,
#     'a': 2,
#     'b': 5,
#     'c': 0
# }



# 1. способ

# test_list = []

# for k, v in test_dict.items():
#     test_list.append((v, k))

# print(max(test_list)[1])


# print(max(test_dict, key=test_dict.get))




matrix_numbers = [
    [15, 2, 7, 8, 9, 10, 3, 5, 14, 11],
    [6, 12, 18, 4, 3, 9, 17, 11, 6, 2],
    [4, 18, 7, 9, 13, 11, 2, 3, 6, 8]
]


# частотность


freq_dict = {}


for i in matrix_numbers:
    for j in i:
        freq_dict[j] = freq_dict.get(j, 0) + 1

print(freq_dict)




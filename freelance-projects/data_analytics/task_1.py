matrix_numbers = [
    [15, 2, 7, 8, 9, 10, 3, 5, 14, 11],
    [6, 12, 18, 4, 3, 9, 17, 11, 6, 2],
    [4, 18, 7, 9, 13, 11, 2, 3, 6, 8]
]

# Initialize variables to store required values
total_sum = 0
max_num = matrix_numbers[0][0]
min_num = matrix_numbers[0][0]
num_frequencies = {}

# Iterate through the matrix to calculate required values
for row in matrix_numbers:
    for num in row:
        total_sum += num
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        num_frequencies[num] = num_frequencies.get(num, 0) + 1

# Find the number with the highest frequency (mode)
mode = max(num_frequencies, key=num_frequencies.get)

# Create the dictionary "description"
description = {
    "sum": total_sum,
    "max": max_num,
    "min": min_num,
    "mode": mode
}

print(description)

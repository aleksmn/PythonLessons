def multiply_range(start, end):
    if start > end:
        start, end = end, start
    result = 1
    for num in range(start, end + 1):
        result *= num
    return result
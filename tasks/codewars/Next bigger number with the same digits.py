def next_bigger(n):
    digits = list(str(n))
    if sorted(digits, reverse=True) == digits:
        return -1

    pos = None

    for i in range(1, len(digits)):
        if digits[-i] > digits[-i-1]:
            pos = -i-1
            break
    if pos is None:
        return -1

    to_swap = -1

    for i in range(pos+1, 0):
        if digits[i] > digits[pos]:
            to_swap = i
    
    digits[to_swap], digits[pos] =  digits[pos], digits[to_swap]

    return int(''.join(digits[:pos+1] + sorted(digits[pos+1:])))

print(next_bigger(4631)) #6134











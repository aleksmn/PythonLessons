from itertools import zip_longest

def sum_digits(x, y, carry):
    answer = int(x) + int(y)
    if carry:
        answer += 1
        carry = False
    if answer > 9:
        carry = True
        answer = answer - 10
    return str(answer), carry

def sum_strings(x, y):
    answer = ''
    carry = False

    for a, b in zip_longest(reversed(x), reversed(y), fillvalue='0'):

        n, carry = sum_digits(a, b, carry)
        answer += n

    if carry:
        answer += '1'
    
    answer = answer.rstrip('0')
    
    if not answer:
        return '0'

    return ''.join(reversed(answer))
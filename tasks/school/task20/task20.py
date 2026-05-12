def max_length_without_ad_da(filename):
    with open(filename, 'r') as f:
        s = f.read().strip()  # если весь файл в одной строке

    n = len(s)
    max_len = 0
    L = 0

    for R in range(n):
        if R > 0 and ((s[R-1] == 'a' and s[R] == 'd') or (s[R-1] == 'd' and s[R] == 'a')):
            L = R  # запрещённая пара, начинаем окно заново с R
        max_len = max(max_len, R - L + 1)

    return max_len


# Пример использования:
if __name__ == "__main__":
    result = max_length_without_ad_da(r"tasks\school\task20\20.txt")
    print(result)

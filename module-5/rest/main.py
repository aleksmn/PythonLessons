def receipt():
    summa = 0
    with open('receipt.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())



receipt()
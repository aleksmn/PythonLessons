'''

Найти решение математического ребуса 
(можно использовать цикл FOR)

  S E N D
+ M O R E
---------
M O N E Y


'''


for s in range(1, 10):
    for e in range(10):
        for n in range(10):
            for d in range(10):
                for m in range(1, 10):
                    for o in range(10):
                        for r in range(10):
                            for y in range(10):
                                if len(set([s, e, n, d, m, o, r, y])) == 8:
                                    send = 1000 * s + 100 * e + 10 * n + d
                                    more = 1000 * m + 100 * o + 10 * r + e
                                    money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                    if send + more == money:
                                        print("S =", s)
                                        print("E =", e)
                                        print("N =", n)
                                        print("D =", d)
                                        print("M =", m)
                                        print("O =", o)
                                        print("R =", r)
                                        print("Y =", y)
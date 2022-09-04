# Python Program to Print Pascal's Triangle
rows = int(input("Enter the number of rows: "))
l = []

for i in range(rows):
    l.append([])
    l[i].append(1)
    for j in range(1, i):
        l[i].append(l[i-1][j-1]+l[i-1][j])
    if (rows != 0):
        l[i].append(1)

for i in range(rows):
    print("   "*(rows-i), end=" ", sep=" ")
    for j in range(0, i+1):
        print("{0:6}".format(l[i][j]), end=" ", sep=" ")
    print()

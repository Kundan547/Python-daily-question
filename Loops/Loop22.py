
n = int (input())
for x in range (1, n + 1, 1):
    for y in range (1, 100, 1):
        z = 3 * y + 2
        if z % 4 != 0:
            print(z, end=' ')
import math
for a in range(1, 5000):
    for b in range(1, a):
        if math.sqrt((a * a) + (b * b)) % 1 == 0:
            c = int(math.sqrt((a * a) + (b * b)))
            print(a, b, c)
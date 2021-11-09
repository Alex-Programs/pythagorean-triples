from numba import njit
import math
import time
import numpy as np
import matplotlib.pyplot as plt

max = input("Maximum: ")
max = int(max)


@njit()
def find_triples(max):
    aResults = []
    cResults = []
    for a in range(2, max):
        for b in range(a, max):
            if a > b:
                continue

            c = math.sqrt((a ** 2) + (b ** 2))
            if c % 1 == 0:
                aResults.append(a)
                cResults.append(c)

    return aResults, cResults


find_triples(50)

start = time.time()
aResults, cResults = find_triples(max)
end = time.time()

print(str(1000 * (end - start)) + " milliseconds")

xpoints = np.array(aResults)
ypoints = np.array(cResults)

plt.scatter(xpoints, ypoints, alpha=100 / max)
plt.xlabel("Values of A")
plt.ylabel("Values of C")
plt.title("A vs C in Pythagoras")

plt.savefig("output.png")
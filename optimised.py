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
    bResults = []
    cResults = []
    for a in range(2, max):
        for b in range(a, max):
            if a > b:
                continue

            c = math.sqrt((a ** 2) + (b ** 2))
            if c % 1 == 0:
                aResults.append(a)
                bResults.append(b)
                cResults.append(c)

    return aResults, bResults, cResults


find_triples(50)

start = time.time()
aResults, bResults, cResults = find_triples(max)
end = time.time()

print(str(1000 * (end - start)) + " milliseconds")


def turn_to_colour(value):
    amount = value / max
    return (amount / 255, 0.5, 0.5)


xpoints = np.array(aResults)
ypoints = np.array(cResults)
print("Processing colours")
start = time.time()
colours = np.array(list(map(turn_to_colour, bResults)))
end = time.time()
delta = (end - start) * 1000
print("Done in " + str(delta) + "ms")

plt.scatter(xpoints, ypoints, alpha=100 / max, c=colours)
plt.xlabel("Values of A")
plt.ylabel("Values of C")
plt.title("A vs C in Pythagoras")

plt.show()

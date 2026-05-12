import matplotlib.pyplot as plt
import numpy as np

R0 = 4
N = 10000

def random_generation(m, a, c):
    results = []
    R1 = (a * R0 + c)%m
    results.append(R1/m)
    for i in range(N):
        R1 = (a * R1 + c)%m
        results.append(R1/m)
    
    return results

def plot_random(m, a, c):
    res = random_generation(m, a, c)
    plt.hist(res)
    plt.show()

plot_random(m = 2**32,
            a = 1664525,
            c = 1013904223
            )
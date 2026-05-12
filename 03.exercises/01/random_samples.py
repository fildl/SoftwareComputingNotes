import numpy as np
import math
import matplotlib.pyplot as plt

def target_pdf(x):
    return x * np.exp(-x)

def make_boxes(target_pdf,
               xlim,n_boxes
               ):

    # estremi dei box
    x_min, x_max = xlim
    edges = np.linspace(x_min, x_max, n_boxes + 1)

    edges_left  = edges[:-1] # tutti gli elementi tranne l'ultimo
    edges_right = edges[1:]  # tutti gli elementi tranne il primo
    box_height = np.zeros(n_boxes)

    for i in range(n_boxes):
        x = np.linspace(edges_left[i], edges_right[i], 100)
        y = target_pdf(x)

        box_height[i] = np.max(y)

    return edges_left, edges_right, box_height

def acceptance_rejection(n_samples,
                         target_pdf,
                         boxes
                         ):
    edges_left, edges_right, box_height = boxes
    
    samples = []

    while len(samples) < n_samples:
        box_index = np.random.randint(0, len(edges_left)) # non serve il +1

        x = np.random.uniform(edges_left[box_index],
                              edges_right[box_index])    
        y = np.random.uniform(0,
                              box_height[box_index]) 

        if y <= target_pdf(x):
            samples.append(x)

    return np.array(samples)

# parametri
xlim = (0, 15)
n_boxes = 10
n_samples = 1000

boxes = make_boxes(target_pdf, xlim, n_boxes)
samples = acceptance_rejection(n_samples, target_pdf, boxes)

# plot
x_plot = np.linspace(xlim[0], xlim[1], 500)
plt.figure(figsize=(10, 6))

# Disegniamo i box (usando i dati spacchettati per chiarezza)
l, r, h = boxes
for i in range(n_boxes):
    plt.plot([l[i], r[i]], [h[i], h[i]], 'r--', alpha=0.5) # Tetto del box
    plt.vlines(l[i], 0, h[i], colors='r', linestyles='--', alpha=0.3)

plt.hist(samples, bins=50, density=True, alpha=0.5, label='Samples (A-R)', color='skyblue')
plt.plot(x_plot, target_pdf(x_plot), 'k-', lw=2, label='Target PDF $p(x)$')

plt.xlabel("x")
plt.ylabel("Densità")
plt.legend()
plt.grid(True, alpha=0.2)
plt.show()
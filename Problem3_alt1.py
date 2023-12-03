import numpy as np
import matplotlib.pyplot as plt
import math

def euler(f, y0, x0, xn, n, forward=True):
    h = (xn - x0) / n if forward else -(xn - x0) / n
    x = np.linspace(x0, xn, n+1)
    y = np.zeros(len(x))
    y[0] = y0

    for i in range(1, len(x)):
        y[i] = y[i-1] + h * f(y[i-1])
    
    return x, y

f = lambda y: math.sqrt(abs(y))

# Experiment with different initial conditions and step sizes
initial_conditions = [1e-4, -1e-4]
step_sizes = [0.01, 0.001]
x_ranges = [(0, 1), (0, -1)]  # Forward and backward integration

plt.figure(figsize=(12, 8))
plt.title("Solution Behavior Near Zero")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

for y0 in initial_conditions:
    for h in step_sizes:
        for x0, xn in x_ranges:
            n = int(abs(xn - x0) / h)
            x, y = euler(f, y0, x0, xn, n, forward=xn > x0)
            plt.plot(x, y, label=f'y0 = {y0}, h = {h}, range = {x0} to {xn}')

plt.legend()
plt.show()

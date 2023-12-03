import numpy as np
import matplotlib.pyplot as plt

# Define the derivative function: y' = y
def derivative(y):
    return y

## Solution 1: Calculate y(2^k) using Forward Euler for k = 1, 2, ... starting at y(0).

# Step size and initial value
h = 1e-3
N = 35

# Iterate for different values of k
for k in range(1, 6):
    x = np.arange(0, 2**k + h, h)
    y = np.zeros(x.shape)
    y[0] = N

    # Euler method
    for i in range(x.shape[0] - 1):
        y[i + 1] = y[i] + h * derivative(y[i])

    # Print the result
    print("y(2^" + str(k) + ") =", y[-1])
    print("x(2^" + str(k) + ") =", x[-1])

## Solution 2: Reuse the calculation for y(2^(k-1)) when calculating y(2^k)

# Step size, initial value, and number of iterations
h = 1e-3
N = 35
iterations = 100

# Create an array to store results
yvec = np.zeros(iterations)
y = N
x = 0

# Iterate for different values of k
for k in range(1, iterations):
    for i in np.arange(x, 2**k, h):
        y = y + h * derivative(y)
        x = x + h

    yvec[k] = y

    # Print the result
    print("y(2^" + str(k) + ") =", y)
    print("x(2^" + str(k) + ") =", x)

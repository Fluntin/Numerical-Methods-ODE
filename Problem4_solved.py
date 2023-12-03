import numpy as np
import matplotlib.pyplot as plt

# Define the derivative function: y' = ky^2
def derivative(y, k):
    return k * y**2

## Forward Euler Method

# Parameters
N = 35
a = 0
b = 10
h = 1e-5
x = np.arange(a, b, h)
y = np.zeros(x.shape[0])

# Initial conditions
epsilon = -1 / h
y[0] = epsilon
k = 1

# Euler
for i in range(y.shape[0] - 1):
    y[i + 1] = y[i] + h * derivative(y[i], k)

## Results

# Plot the result
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y(x)')
plt.axhline(0, color='red', linestyle='--', label='y=0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y(x) using Forward Euler Method')
plt.grid(True)
plt.legend()

# Estimate the x-coordinate of the singularity
t = 1e8
pang = 0
for i in range(y.shape[0]):
    if y[i] > t:
        pang = i
        break
print("Estimated x-coordinate of singularity:", x[pang])

# Optionally, you can add a scatter plot of points up to the singularity
# plt.scatter(x[0:pang], y[0:pang], color='green', marker='o', label='Points up to singularity')
# plt.legend()

plt.show()

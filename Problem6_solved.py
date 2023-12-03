import numpy as np
import matplotlib.pyplot as plt

# Define the system of differential equations
# x_0' = x_1
# x_1' = -x_0
def f(x):
    x_prime = np.zeros(2)
    x_prime[0] = x[1]
    x_prime[1] = -x[0]
    return x_prime

## Runge-Kutta (RK4) method to approximate the root closest to t=1e3
h = 1e-3
t = np.arange(0, 1e3 + 1, h)
n = len(t)
x = np.zeros((2, n))
x[0, 0] = 1

# Main loop
for i in range(len(t) - 1):
    k1 = f(x[:, i])
    k2 = f(x[:, i] + (h / 2) * k1)
    k3 = f(x[:, i] + (h / 2) * k2)
    k4 = f(x[:, i] + h * k3)
    x[:, i + 1] = x[:, i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    # Check if x[1, i] becomes negative after t=1e3
    if x[1, i] < 0 and t[i] > 1e3:
        last_i = i
        break

# Determine the closest index
if np.abs(x[0, last_i - 1]) < np.abs(x[0, last_i]):
    closest_i = last_i
else:
    closest_i = last_i - 1

## Print the result
print("Approximation of π:", t[closest_i] / 318.5)
print("Actual value of π:", np.pi)

# Plot the results
plt.plot(t, x[0, :])
plt.xlabel('t')
plt.ylabel('x[0]')
plt.title('Approximation of π using RK4')
plt.show()

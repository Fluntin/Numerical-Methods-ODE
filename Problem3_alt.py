import numpy as np
import matplotlib.pyplot as plt
import math

def euler(f, y0, x0, xn, n):
    """
    Euler's method for solving differential equations.
    :param f: The function defining the differential equation y' = f(y).
    :param y0: Initial value of y.
    :param x0: Initial value of x.
    :param xn: Final value of x.
    :param n: Number of steps.
    :return: Arrays of x and y values.
    """
    h = (xn - x0) / n  # Calculate step size
    x = np.linspace(x0, xn, n+1)  # Generate x values
    y = np.zeros(len(x))  # Initialize y array
    y[0] = y0  # Set initial condition

    for i in range(1, len(x)):
        y[i] = y[i-1] + h * f(y[i-1])  # Euler's method update

    return x, y

# Define the differential equation y' = sqrt(|y|)
f = lambda y: math.sqrt(abs(y))

# Parameters for Euler's method
x0 = -1   # Starting point for x
xn = 1   # Ending point for x
n = 3  # Number of steps

# Initial conditions to explore
initial_conditions = [1e-308, 1e-10, 0, -1e-10, -1e-308]

# Plotting
plt.figure(figsize=(10, 6))
plt.title("Solution of y' = sqrt(|y|) for different initial conditions")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# Apply Euler's method for each initial condition and plot
for y0 in initial_conditions:
    x, y = euler(f, y0, x0, xn, n)
    plt.plot(x, y, label=f'y0 = {y0}')

plt.legend()
plt.show()

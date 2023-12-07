import numpy as np
import matplotlib.pyplot as plt

def derivative(y):
    return np.sqrt(np.abs(y))

def forward_euler(y_initial, step_size, start, end):
    num_points = int((end - start) / step_size) + 1
    time_points = np.linspace(start, end, num_points)
    y_values = np.zeros(len(time_points))
    y_values[0] = y_initial

    for i in range(1, len(time_points)):
        y_values[i] = y_values[i - 1] + step_size * derivative(y_values[i - 1])

    return time_points, y_values

# Parameters
step_size = 1
start = -4
end = 4
epsilon = 0.00000001
initial_conditions = [-1, -2, -3, -4]  # Adjusted initial conditions
threshold = 1e-4  # Define a threshold for convergence

# Determine the layout of subplots
num_plots = len(initial_conditions)
rows = int(np.ceil(num_plots / 2))
cols = 2 if num_plots > 1 else 1

# Create a separate subplot for each initial condition
plt.figure(figsize=(10, rows * 4))
for idx, y0 in enumerate(initial_conditions):
    plt.subplot(rows, cols, idx + 1)
    time_points, y_values = forward_euler(y0, step_size, start, end)

    plt.plot(time_points, y_values, label=f'y0 = {y0}')
    plt.axhline(0, color='red', linestyle='--', label='y=0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'y0 = {y0}')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

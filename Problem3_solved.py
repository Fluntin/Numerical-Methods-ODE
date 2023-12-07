import numpy as np
import matplotlib.pyplot as plt

# Define the derivative function: y' = sqrt(abs(y))
def derivative(y):
    return np.sqrt(np.abs(y))

# Forward Euler Method

# Initial values
step_size = 1
epsilon = 0.00000001
start = -5
end = 5

# Arrays
time_points = np.arange(start, end, step_size)
y_values = np.zeros(time_points.shape)
y_values[0] = -1 + epsilon
converged_points_count = 0
converged_points = []

# Main loop
for i in range(y_values.shape[0] - 1):
    y_values[i + 1] = y_values[i] + step_size * derivative(y_values[i])
    if abs(y_values[i + 1]) <= 1e-4:
        converged_points.append(time_points[i + 1])
        converged_points_count += 1

# Results
print("Converged between:", converged_points[0], converged_points[-1])
print("Converged", converged_points_count, "times")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(time_points, y_values, label='y(x)')
plt.axhline(0, color='red', linestyle='--', label='y=0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y(x) using Forward Euler Method')
plt.grid(True)
plt.legend()
plt.show()


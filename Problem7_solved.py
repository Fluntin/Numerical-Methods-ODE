import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITATIONAL_CONSTANT = 39
SUN_MASS = 1

# Time parameters
time_step = 0.001
time_max = 10

# Initial conditions for Earth
earth_initial_position = [1, 0]
earth_initial_velocity = [0, 6.28]

# Function to calculate velocity derivative
def calculate_velocity_derivative(position):
    return -position * (GRAVITATIONAL_CONSTANT * SUN_MASS / np.linalg.norm(position) ** 3)

# Time array
time_array = np.arange(0, time_max, time_step)

# Earth's trajectory
earth_position = np.zeros((2, len(time_array)))
earth_velocity = np.array(earth_initial_velocity)
earth_position[:, 0] = np.array(earth_initial_position)

# Calculating Earth's position over time
for i in range(len(time_array) - 1):
    earth_velocity += time_step * calculate_velocity_derivative(earth_position[:, i])
    earth_position[:, i + 1] = earth_position[:, i] + time_step * earth_velocity

# Plotting
plt.figure(figsize=(8, 6))  # Adjust figure size for better visibility
plt.plot(earth_position[0, :], earth_position[1, :], label='Earth Orbit', color='blue')

# Sun representation
plt.scatter(0, 0, color='#ffef63', s=100)  # Sun as a larger point for visibility

# Setting aspect ratio, grid, labels, and title
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Simulation of Earth Orbit')

# Show plot
plt.show()

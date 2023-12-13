import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITATIONAL_CONSTANT = 39
SUN_MASS = 1
EARTH_MASS = 1 / 332946
JUPITER_MASS = 318 * EARTH_MASS

# Time parameters
time_step = 1e-3
time_max = 12

# Initial conditions for Earth
earth_initial_position = [1, 0]
earth_initial_velocity = [0, 6.28]

# Initial conditions for Jupiter
jupiter_initial_position = [5.1, 0]
jupiter_initial_velocity = [0, 0.44 * 6.28]

# Function to calculate velocity derivative
def calculate_velocity_derivative(position):
    return -position * (GRAVITATIONAL_CONSTANT * SUN_MASS / np.linalg.norm(position) ** 3)

# Time array
time_array = np.arange(0, time_max, time_step)

# Earth's trajectory
earth_position = np.zeros((2, len(time_array)))
earth_velocity = np.array(earth_initial_velocity)
earth_position[:, 0] = np.array(earth_initial_position)

# Jupiter's trajectory
jupiter_position = np.zeros((2, len(time_array)))
jupiter_velocity = np.array(jupiter_initial_velocity)
jupiter_position[:, 0] = np.array(jupiter_initial_position)

# Calculating positions over time
for i in range(len(time_array) - 1):
    earth_velocity += time_step * calculate_velocity_derivative(earth_position[:, i])
    earth_position[:, i + 1] = earth_position[:, i] + time_step * earth_velocity

    jupiter_velocity += time_step * calculate_velocity_derivative(jupiter_position[:, i])
    jupiter_position[:, i + 1] = jupiter_position[:, i] + time_step * jupiter_velocity

# Space probe initial conditions
probe_initial_position = [1.001, 0]
escape_velocity = np.sqrt(2 * GRAVITATIONAL_CONSTANT * SUN_MASS / (np.linalg.norm(probe_initial_position)))

probe_initial_velocity = [7.589, np.sqrt((escape_velocity - 0.4) ** 2 - 7.589 ** 2)]
probe_position = np.zeros((2, len(time_array)))
probe_velocity = np.array(probe_initial_velocity)
probe_position[:, 0] = np.array(probe_initial_position)

# Function to calculate probe's velocity derivative
def calculate_probe_velocity_derivative(probe_pos, earth_pos, jupiter_pos):
    r1 = earth_pos - probe_pos
    r2 = jupiter_pos - probe_pos
    return GRAVITATIONAL_CONSTANT * (
        -probe_pos * SUN_MASS / np.linalg.norm(probe_pos) ** 3
        + r1 * EARTH_MASS / np.linalg.norm(r1) ** 3
        + r2 * JUPITER_MASS / np.linalg.norm(r2) ** 3
    )

# Calculating probe trajectory
for i in range(len(time_array) - 1):
    probe_velocity += time_step * calculate_probe_velocity_derivative(probe_position[:, i], earth_position[:, i], jupiter_position[:, i])
    probe_position[:, i + 1] = probe_position[:, i] + time_step * probe_velocity

import matplotlib.pyplot as plt

# Use a different style for better aesthetics
plt.style.use('seaborn-darkgrid')

# Plotting with improved aesthetics
fig, ax = plt.subplots(figsize=(10, 8))

# Swap X and Y coordinates and customize line styles
ax.plot(earth_position[1, :], earth_position[0, :], label='Earth Orbit', color='blue', linewidth=2, linestyle='--')
ax.plot(jupiter_position[1, :], jupiter_position[0, :], label='Jupiter Orbit', color='orange', linewidth=2, linestyle='--')
ax.plot(probe_position[1, :], probe_position[0, :], label='Spacecraft Trajectory', color='purple', linewidth=2)

# Customize the Sun marker
ax.scatter(0, 0, color='gold', s=200, marker='o', label='Sun')

# Set equal aspect ratio and adjust axis limits if needed
ax.set_aspect('equal', adjustable='box')

# Customize plot labels and title
ax.set_xlabel('Y Coordinate')
ax.set_ylabel('X Coordinate')
ax.set_title('Simulation of Orbits and Spacecraft Trajectory')

# Add a legend with improved placement
ax.legend(loc='upper right')

# Customize background color
ax.set_facecolor('lightgray')

# Remove top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Display the plot
plt.show()




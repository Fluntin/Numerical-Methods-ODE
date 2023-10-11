import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITY_CONSTANT = 6.67430e-11
M_Sun = 1.989e30
AU = 1.496e11 
YEAR_IN_SECONDS = 365.0 * 24.0 * 3600.0
EARTH_ORBITAL_VELOCITY = 29783.0

# Gravitational acceleration due to the Sun
def gravitational_acceleration(x, y):
    distance = np.sqrt(x**2 + y**2)
    ax = -(GRAVITY_CONSTANT * M_Sun * x) / distance**3
    ay = -(GRAVITY_CONSTANT * M_Sun * y) / distance**3
    return ax, ay

# Symplectic Euler method for orbit calculations
def symplectic_euler(time_step, total_time):
    steps = int(total_time / time_step)
    x, y, vx, vy = np.zeros(steps), np.zeros(steps), np.zeros(steps), np.zeros(steps)
    x[0], y[0], vx[0], vy[0] = AU, 0, 0, EARTH_ORBITAL_VELOCITY
    
    for i in range(steps - 1):
        ax, ay = gravitational_acceleration(x[i], y[i])
        vx[i+1] = vx[i] + time_step * ax
        vy[i+1] = vy[i] + time_step * ay
        x[i+1] = x[i] + time_step * vx[i+1]
        y[i+1] = y[i] + time_step * vy[i+1]

    return x, y, vx, vy

# Time parameters
total_time = 20 * YEAR_IN_SECONDS
time_step = YEAR_IN_SECONDS / 365  # One day per step

# Simulate using symplectic Euler method
x, y, vx, vy = symplectic_euler(time_step, total_time)

# Compute total energy
E = 0.5 * (vx**2 + vy**2) - (GRAVITY_CONSTANT * M_Sun) / np.sqrt(x**2 + y**2)

# Plotting
# Set a better plot style
plt.style.use('ggplot')

# Plotting
plt.figure(figsize=(14, 7))

# Orbit plot
plt.subplot(1, 2, 1)
plt.plot(x, y, linewidth=2, color='blue', label='Earth Orbit')
plt.scatter(0, 0, color='yellow', s=300, label="Sun")  # Position of the Sun
plt.title('Earth Orbit around the Sun - Symplectic Euler', fontsize=16)
plt.xlabel('X-position [m]', fontsize=14)
plt.ylabel('Y-position [m]', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Energy plot
plt.subplot(1, 2, 2)
time_values = np.arange(0, total_time, time_step)[:len(E)]
plt.plot(time_values, E, linewidth=2, color='green', label='Total Energy')
plt.title('Total Energy E(t) over time - Symplectic Euler', fontsize=16)
plt.xlabel('Time [s]', fontsize=14)
plt.ylabel('E(t)', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.show()
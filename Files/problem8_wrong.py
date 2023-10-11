import numpy as np
import matplotlib.pyplot as plt

def gravitational_force(x_position_earth, x_velocity_earth, y_position_earth, y_velocity_earth,
                        x_position_jupiter, x_velocity_jupiter, y_position_jupiter, y_velocity_jupiter,
                        x_position_satellite, x_velocity_satellite, y_position_satellite, y_velocity_satellite):
    return np.array([
        # Forces on Earth
        x_velocity_earth, -G * (mass_sun * x_position_earth / (x_position_earth**2 + y_position_earth**2)**(3/2) + mass_jupiter * (x_position_earth - x_position_jupiter) / ((x_position_earth - x_position_jupiter)**2 + (y_position_earth - y_position_jupiter)**2)**(3/2) + mass_satellite * (x_position_earth - x_position_satellite) / ((x_position_earth - x_position_satellite)**2 + (y_position_earth - y_position_satellite)**2)**(3/2)),
        y_velocity_earth, -G * (mass_sun * y_position_earth / (x_position_earth**2 + y_position_earth**2)**(3/2) + mass_jupiter * (y_position_earth - y_position_jupiter) / ((x_position_earth - x_position_jupiter)**2 + (y_position_earth - y_position_jupiter)**2)**(3/2) + mass_satellite * (y_position_earth - y_position_satellite) / ((x_position_earth - x_position_satellite)**2 + (y_position_earth - y_position_satellite)**2)**(3/2)),

        # Forces on Jupiter
        x_velocity_jupiter, -G * (mass_sun * x_position_jupiter / (x_position_jupiter**2 + y_position_jupiter**2)**(3/2) + mass_earth * (x_position_jupiter - x_position_earth) / ((x_position_jupiter - x_position_earth)**2 + (y_position_jupiter - y_position_earth)**2)**(3/2) + mass_satellite * (x_position_jupiter - x_position_satellite) / ((x_position_jupiter - x_position_satellite)**2 + (y_position_jupiter - y_position_satellite)**2)**(3/2)),
        y_velocity_jupiter, -G * (mass_sun * y_position_jupiter / (x_position_jupiter**2 + y_position_jupiter**2)**(3/2) + mass_earth * (y_position_jupiter - y_position_earth) / ((x_position_jupiter - x_position_earth)**2 + (y_position_jupiter - y_position_earth)**2)**(3/2) + mass_satellite * (y_position_jupiter - y_position_satellite) / ((x_position_jupiter - x_position_satellite)**2 + (y_position_jupiter - y_position_satellite)**2)**(3/2)),

        # Forces on Satellite
        x_velocity_satellite, -G * (mass_sun * x_position_satellite / (x_position_satellite**2 + y_position_satellite**2)**(3/2) + mass_earth * (x_position_satellite - x_position_earth) / ((x_position_satellite - x_position_earth)**2 + (y_position_satellite - y_position_earth)**2)**(3/2) + mass_jupiter * (x_position_satellite - x_position_jupiter) / ((x_position_satellite - x_position_jupiter)**2 + (y_position_satellite - y_position_jupiter)**2)**(3/2)),
        y_velocity_satellite, -G * (mass_sun * y_position_satellite / (x_position_satellite**2 + y_position_satellite**2)**(3/2) + mass_earth * (y_position_satellite - y_position_earth) / ((x_position_satellite - x_position_earth)**2 + (y_position_satellite - y_position_earth)**2)**(3/2) + mass_jupiter * (y_position_satellite - y_position_jupiter) / ((x_position_satellite - x_position_jupiter)**2 + (y_position_satellite - y_position_jupiter)**2)**(3/2))])


def runge_kutta_method(initial_state, h, cap):
    t = 0
    x1s, y1s, x2s, y2s, x3s, y3s, ts = [initial_state[0]], [initial_state[2]], [initial_state[4]], [initial_state[6]], [initial_state[8]], [initial_state[10]], [t]

    while t < cap:
        k1 = h * gravitational_force(*initial_state)
        k2 = h * gravitational_force(*(initial_state + k1 / 2))
        k3 = h * gravitational_force(*(initial_state + k2 / 2))
        k4 = h * gravitational_force(*(initial_state + k3))

        initial_state = initial_state + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h

        x1s.append(initial_state[0])
        y1s.append(initial_state[2])
        x2s.append(initial_state[4])
        y2s.append(initial_state[6])
        x3s.append(initial_state[8])
        y3s.append(initial_state[10])
        ts.append(t)

    return x1s, y1s, x2s, y2s, x3s, y3s, ts

#Space Contstants
G = 6.67428e-11 # gravitational constant in m^3 kg^-1 s^-2
AU = 1496e8 # 1 AU in meters

# Masses
mass_sun = 1.98892e30  # mass of the Sun in kg
mass_earth = 5.9742e24  # mass of Earth in kg
mass_jupiter = 1.89813e27  # mass of Jupiter in kg
mass_satellite = 1e3  # mass of a satellite in kg

# Initial conditions
# Earth
x_position_earth = -1*AU
x_velocity_earth = 0
y_position_earth = 0
y_velocity_earth = 29783

# Jupiter
x_position_jupiter = 0
x_velocity_jupiter = 17020
y_position_jupiter = 3*AU
y_velocity_jupiter = 0

# Satellite
x_position_satellite = -1.1*AU
x_velocity_satellite = 0
y_position_satellite = 0
y_velocity_satellite = 34500 

T = 3.1536e7 * 15  # 1 year in seconds multiplied by 15 (15 years)
dt = 1e3  # Time step (for example)

initial_conditions = np.array([x_position_earth, x_velocity_earth, y_position_earth, y_velocity_earth, x_position_jupiter, x_velocity_jupiter, y_position_jupiter, y_velocity_jupiter, x_position_satellite, x_velocity_satellite, y_position_satellite, y_velocity_satellite])

# Runge-Kutta
x1s, y1s, x2s, y2s, x3s, y3s, ts = runge_kutta_method(initial_conditions, dt, T)

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(x1s, y1s, label="Earth's Orbit")
plt.plot(x2s, y2s, label="Jupiter's Orbit")
plt.plot(x3s, y3s, label="Satellite's Trajectory", linestyle='--', color='cyan')
plt.scatter(0, 0, c='yellow', s=500, label='Sun', zorder=5)  # Sun at (0,0)
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()
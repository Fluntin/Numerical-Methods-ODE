import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M_sun = 1.989e30
AU = 1.496e11
epsilon = 1e6  # Softening parameter
m_jupiter = 1.898e27  # mass of Jupiter

def acceleration_jupiter(x, y):
    r = np.sqrt(x**2 + y**2)
    ax = -G * M_sun * x / (r**2 + epsilon**2)**(1.5)
    ay = -G * M_sun * y / (r**2 + epsilon**2)**(1.5)
    return ax, ay

def acceleration_earth(x, y, x_j, y_j):
    r = np.sqrt(x**2 + y**2)
    r_j = np.sqrt((x - x_j)**2 + (y - y_j)**2)
    ax = -G * M_sun * x / (r**2 + epsilon**2)**(1.5) + G * m_jupiter * (x - x_j) / (r_j**2 + epsilon**2)**(1.5)
    ay = -G * M_sun * y / (r**2 + epsilon**2)**(1.5) + G * m_jupiter * (y - y_j) / (r_j**2 + epsilon**2)**(1.5)
    return ax, ay

def symplectic_euler(dt, T, x0, y0, vx0, vy0, is_earth=False, x_jupiter=None, y_jupiter=None):
    N = int(T/dt)
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    x[0], y[0], vx[0], vy[0] = x0, y0, vx0, vy0
    for i in range(N-1):
        if is_earth:
            ax, ay = acceleration_earth(x[i], y[i], x_jupiter[i], y_jupiter[i])
        else:
            ax, ay = acceleration_jupiter(x[i], y[i])
        
        vx[i+1] = vx[i] + dt * ax
        vy[i+1] = vy[i] + dt * ay
        x[i+1] = x[i] + dt * vx[i+1]
        y[i+1] = y[i] + dt * vy[i+1]
    return x, y, vx, vy

# Jupiter's initial conditions for an elliptical orbit
x0_jupiter = 5.5*AU
y0_jupiter = 0
vx0_jupiter = 0
vy0_jupiter = np.sqrt(G * M_sun * (2 / x0_jupiter - 1 / (5.2*AU)))

#Time parameters
T = 13*365.0*24.0*3600.0
year_in_sec = 365.0 * 24.0 * 3600.0
dt = year_in_sec / 10000

x_jupiter, y_jupiter, vx_jupiter, vy_jupiter = symplectic_euler(dt, T, x0_jupiter, y0_jupiter, vx0_jupiter, vy0_jupiter)

# Earth's initial conditions for an elliptical orbit
x0_earth = 1.05*AU
y0_earth = 0
vx0_earth = 0
vy0_earth = 35e3

x_earth, y_earth, vx_earth, vy_earth = symplectic_euler(dt, T, x0_earth, y0_earth, vx0_earth, vy0_earth, True, x_jupiter, y_jupiter)

plt.figure(figsize=(10, 10))
plt.plot(x_earth, y_earth, label="Earth's Orbit")
plt.plot(x_jupiter, y_jupiter, label="Jupiter's Orbit")
plt.scatter(0, 0, c='yellow', s=500, label='Sun', zorder=5)  # Sun at (0,0)
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()
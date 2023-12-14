import math
import numpy as np
import matplotlib.pyplot as plt

# Function describing the differential equation du/dt = -u
def f(t, u):
    return -u

# Exact solution for comparison
def exact_solution(u0, du0, t):
    return u0 * math.cos(t) + du0 * math.sin(t)

# Function to iteratively solve the differential equation
def iterate(func, u, v, tmax, n):
    dt = tmax / (n - 1)
    t = 0

    for _ in range(n):
        u, v = func(u, v, t, dt)
        t += dt

    return u

# Euler method for a single time step
def euler_step(u, v, t, dt):
    v_new = v + dt * f(t, u)
    u_new = u + dt * v
    return u_new, v_new

# Runge-Kutta method for a single time step
def runge_kutta_step(u, v, t, dt):
    k1 = f(t, u)
    k2 = f(t + dt * 0.5, u + k1 * 0.5 * dt)
    k3 = f(t + dt * 0.5, u + k2 * 0.5 * dt)
    k4 = f(t + dt, u + k3 * dt)

    v += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    k1 = k2 = k3 = k4 = v

    u += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return u, v

# Function to solve using Euler's method
def euler_solver(u0, v0, tmax, n):
    return iterate(euler_step, u0, v0, tmax, n)

# Function to solve using Runge-Kutta method
def runge_kutta_solver(u0, v0, tmax, n):
    return iterate(runge_kutta_step, u0, v0, tmax, n)

# Function to plot the results
def plot_results(u0, v0, tmax, n):
    dt = tmax / (n - 1)
    t = 0
    allt = []
    error_euler = []
    error_rk = []
    exact_values = []
    euler_values = []
    rk_values = []

    u_exact = u_euler = u_rk = u0
    v_exact = v_euler = v_rk = v0

    for _ in range(n):
        u_exact = exact_solution(u0, v0, t)
        u_euler, v_euler = euler_step(u_euler, v_euler, t, dt)
        u_rk, v_rk = runge_kutta_step(u_rk, v_rk, t, dt)
        allt.append(t)
        error_euler.append(abs(u_euler - u_exact))
        error_rk.append((u_rk - u_exact))
        exact_values.append(u_exact)
        euler_values.append(u_euler)
        rk_values.append(u_rk)
        t += dt

    # Create a single figure with subplots
    plt.figure(figsize=(10, 6))

    # Plot Error
    plt.subplot(2, 1, 1)
    plt.title("Error")
    plt.ylabel("Error")
    plt.xlabel("t")

    #plt.plot(allt, error_euler, 'tab:orange', label="Euler", linewidth=2)
    plt.plot(allt, error_rk, 'b', label="Runge-Kutta", linewidth=2)

    plt.legend(loc='upper right')
    plt.grid(True)

    # Plot Result
    plt.subplot(2, 1, 2)
    plt.title("Error")
    plt.ylabel("y(t)")
    plt.xlabel("t")

    #plt.plot(allt, euler_values, 'tab:orange', label="Euler", linewidth=2)
    plt.plot(allt, rk_values, 'b', label="Runge-Kutta", linewidth=2)
    plt.plot(allt, exact_values, 'purple', label="Exact", linewidth=2)

    plt.legend(loc='upper right')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Initial conditions
u0 = 1
v0 = 0

# Change tmax to 1000 and increase the number of steps for better resolution
tmax = 1000
n = 10000

# Solve using Euler's method
euler_solver(u0, v0, tmax, n)

# Solve using Runge-Kutta method
runge_kutta_solver(u0, v0, tmax, n)

# Plot the results over the extended time frame
plot_results(u0, v0, tmax, n)


import math 
import time
import numpy as np
import matplotlib.pyplot as plt

def differential_equation(x, y, C):
    return C * y ** 2

def  euler_forward_problem4_C(f, C):

    step_size = 1
    time_start = 0
    time_end = 1e5
    initial_value = -1e-6
    time_points = [time_start]
    solution_values = [initial_value]

    while time_points[-1] < time_end:
        next_time = time_points[-1] + step_size
        next_value = solution_values[-1] + step_size * f(time_points[-1], solution_values[-1], C)
        time_points.append(next_time)
        solution_values.append(next_value)

    return time_points, solution_values

def plot_solution():
    import matplotlib.pyplot as plt

    C_values = [10, 50, 75, 100, 250, 500, 1000, 1250, 1500]
    for C in C_values:
        x_vals, y_vals = euler_forward_problem4_C(differential_equation, C)
        plt.plot(x_vals, y_vals, label=f"C = {C}")

    plt.grid(True)
    plt.title("Numerical Solution of y' = Cy^2 using Euler Forward")
    plt.legend()
    plt.show()

# Call the function to run the program
plot_solution()

def differential_equation(x, y, C):
    return C * y ** 2

def rk4(f, C):
    step_size = 1
    time_start = 0
    time_end = 1e5
    initial_value = -1e-6
    time_points = [time_start]
    solution_values = [initial_value]

    while time_points[-1] < time_end:
        t = time_points[-1]
        y = solution_values[-1]
        
        k1 = step_size * f(t, y, C)
        k2 = step_size * f(t + 0.5 * step_size, y + 0.5 * k1, C)
        k3 = step_size * f(t + 0.5 * step_size, y + 0.5 * k2, C)
        k4 = step_size * f(t + step_size, y + k3, C)

        next_value = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        next_time = t + step_size

        time_points.append(next_time)
        solution_values.append(next_value)

    return time_points, solution_values

def plot_solution():

    C_values = [100, 1000, 1950, 1975, 2000]
    for C in C_values:
        x_vals, y_vals = rk4(differential_equation, C)
        plt.plot(x_vals, y_vals, label=f"C = {C}")

    plt.grid(True)
    plt.title("Numerical Solution of y' = Cy^2 using RK4")
    plt.legend()
    plt.show()

# Call the function to run the program
plot_solution()
import math 
import time
import numpy as np
import matplotlib.pyplot as plt

# The function then returns whether the goal was exactly met 
def rk_4_for_problem5(f, y0, t_start, goal_value, h):
    
    # f is the function to integrate
    # y0 is the initial value
    # t_start is the start time
    # t_stop is the stop time
    # h is the step size 
    
    t_value = [t_start]
    y_value = [y0]
    
    # Here I define a condition that will tell me if the goal is met
    condition = True
    
    #We keep looping until the condition is false
    while condition:
        
        k1 = f(t_value[-1], y_value[-1])
        k2 = f(t_value[-1] + h/2, y_value[-1] + h/2 * k1)
        k3 = f(t_value[-1] + h/2, y_value[-1] + h/2 * k2)
        k4 = f(t_value[-1] + h, y_value[-1] + h * k3)
        
        t_next = t_value[-1] + h
        y_next = y_value[-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        
        t_value.append(t_next)
        y_value.append(y_next)

        # Check if the goal is met exactly
        if round(y_value[-1], 2) == round(goal_value, 2):
            # I return the last value of y where we met the goal.
            return condition, y_value[-1]
        
        #Check if we overshot the goal
        if round(y_value[-1], 2) >= round(goal_value, 2):
            condition = False
            # I return the last value of y before we overshot the goal
            return condition, y_value[-1]
        
def euler_forward_for_problem5(initial_time, initial_value, power, step_size):
    
    stopping_time = 2**power
    current_time = initial_time
    current_value = initial_value

    while current_time < stopping_time:
        current_time += step_size
        current_value += step_size * current_value
        
    return current_value

def f(t,y): 
    return y

# This is the analytical solution
def y(t):
    return 72* np.exp(t)

N = 100
y0 = 72
t_start = 0

rk4_errors = []
euler_errors = []

# Using linspace to generate values between 0 and 4, inclusive, with a desired number of points
num_points = 100
k_values = np.linspace(0, 4, num_points)

for k in k_values:
    # Define my goal value
    goal_value = y(2**k)
    # ... (rest of your loop logic)
    # I want to be able to adjust the step size so that I can get closer to the goal value
    h = (2**k - t_start) / N

    condition, y_value_rk4 = rk_4_for_problem5(f, y0, t_start, goal_value, h)
    y_value_euler = euler_forward_for_problem5(t_start, y0, k, h)
    
    # Keep trying with a smaller step until the condition becomes True
    while not condition:
        N = N * 1e3
        h = (2**k - t_start) / N
        condition, y_value_rk4 = rk_4_for_problem5(f, y0, t_start, goal_value, h)
        y_value_euler = euler_forward_for_problem5(t_start, y0, k, h)
    
    # Compute the errors for this k and append to the lists
    rk4_error = abs(goal_value - y_value_rk4)
    euler_error = abs(goal_value - y_value_euler)

    rk4_errors.append(rk4_error)
    euler_errors.append(euler_error)

plt.figure(figsize=(10,6))
plt.plot(k_values, rk4_errors, '-o', label='RK4 Errors', markersize=4)
plt.plot(k_values, euler_errors, '-x', label="Euler's Method Errors", markersize=4)
plt.xlabel('k values')
plt.ylabel('Error')
plt.title('Error of RK4 and Euler methods vs k values')
plt.yscale('log')  # Use a logarithmic scale on the y-axis to better visualize the errors
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()
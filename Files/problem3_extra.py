import math 
import time
import numpy as np
import matplotlib.pyplot as plt

# Assume that I have several points to test.

# I define my initial conditions
y1_initial=0
y2_initial=0+1e-10
y3_initial=0+1e-5
y4_initial=0-1e-7
y5_initial=0-1e-3

# I have my function
def f(t, y):
    return np.sqrt(abs(y))

#This is just my general Euler forward function
def forward_euler_problem3(f, y_initial, t_start, t_stop, h):
    
    t_values = [t_start]
    y_values = [y_initial]

    while t_values[-1] < t_stop:
        t_next = t_values[-1] + h
        y_next = y_values[-1] + h * f(t_values[-1], y_values[-1])

        t_values.append(t_next)
        y_values.append(y_next)

    return t_values, y_values

# Get the values for y1, y2, y3, y4, y5
y1_values = forward_euler_problem3(f, y1_initial, 0, 1, 0.1)
y2_values = forward_euler_problem3(f, y2_initial, 0, 1, 0.1)
y3_values = forward_euler_problem3(f, y3_initial, 0, 1, 0.1)
y_4values = forward_euler_problem3(f, y4_initial, 0, 1, 0.1)
y_5values = forward_euler_problem3(f, y5_initial, 0, 1, 0.1)

# I plot the graphs
# I plot the graphs
plt.figure(figsize=(10, 6))
plt.title('Impact of Varying Initial Conditions on y over Time', fontsize=16)
plt.plot(y1_values[0], y1_values[1], color='blue', linestyle='-', linewidth=2, label='y1 vs. t')
plt.plot(y2_values[0], y2_values[1], color='red', linestyle='-', linewidth=2, label='y2 vs. t')
plt.plot(y3_values[0], y3_values[1], color='green', linestyle='-', linewidth=2, label='y3 vs. t')
plt.plot(y_4values[0], y_4values[1], color='black', linestyle='-', linewidth=2, label='y4 vs. t')
plt.plot(y_5values[0], y_5values[1], color='yellow', linestyle='-', linewidth=2, label='y5 vs. t')
plt.xlabel('Time', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='best', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
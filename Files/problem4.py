import math 
import time
import numpy as np
import matplotlib.pyplot as plt

# This is a slightly modified version of the RK4 function that I used for the problem4

def rk_4_for_problem4(f, y0, t_start, t_stop, h):
    
    # f is the function to integrate
    # y0 is the initial value
    # t_start is the start time
    # t_stop is the stop time
    # h is the step size 
    
    t_value = [t_start]
    y_value = [y0]
    
    # sample_t is the list of time values
    # sample_y is the list of y values
    # the sample_t and sample_y are the values that satisfy the condition y(t) = 0
    
    while t_value[-1] < t_stop:
        k1 = f(t_value[-1], y_value[-1])
        k2 = f(t_value[-1] + h/2, y_value[-1] + h/2 * k1)
        k3 = f(t_value[-1] + h/2, y_value[-1] + h/2 * k2)
        k4 = f(t_value[-1] + h, y_value[-1] + h * k3)
        
        t_next = t_value[-1] + h
        y_next = y_value[-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        
        t_value.append(t_next)
        y_value.append(y_next)
        
        # I define this arbitrary value 1e10 to tell me that the function is diverging
        # This arbitrary restrtion should give me my time to singularity, given my stepsize is also nice and small.
        if y_next > 1e10:
            break
    
    return t_value, y_value

# Define the function
def f(t,y):
    return y**2

#Initial conditions
N=72
y0 = N / 100
t_start = 0
t_stop = 5
h = (t_stop - t_start) / 1000

# Return evenly spaced numbers over a specified interval.
t_values = np.arange(0, t_stop, h)
y_values = []

#Kick off the loop
y = y0

for t in t_values:
    y_values.append(y)
    y += h * y**2
    # I define this arbitrary value 1e50 to stop the loop as blowing up
    if abs(y) > 1e50:
        print("Solution is growing too rapidly. Stopping integration.")
        break

t_values = t_values[:len(y_values)]

#Initial conditions
N=72
y0 = N / 100
t_start = 0
t_stop = 10
h = (t_stop - t_start) / 100000

t,y=rk_4_for_problem4(f, y0, t_start, t_stop, h)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t_values[:len(y_values)], y_values, label=f'N = {N}', color='b', linewidth=2)
plt.xlabel('Time (t)', fontsize=14)
plt.ylabel('y(t)', fontsize=14)
plt.title("Numerical Solution of $y' = y^2$", fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print("Estimated time to singularity:", t[-1])
import math 
import time
import numpy as np
import matplotlib.pyplot as plt

# This is a slightly modified version of the RK4 function that I used for the problem3

def rk_4_for_problem3(f, y0, t_start, t_stop, h):
    
    # f is the function to integrate
    # y0 is the initial value
    # t_start is the start time
    # t_stop is the stop time
    # h is the step size
    
    t_value = [t_start]
    y_value = [y0]
    sample_t = []
    sample_y = []
    
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
        
        # I added this to check if y deviates from 0
        if y_next > 1e-4:
            break
        
        if abs(y_next) < 1e-4:
            sample_t.append(t_next)
            sample_y.append(y_next)
    
    return sample_t, sample_y

# Define the function
def f(t, y):
    return np.sqrt(abs(y))

t_start = -1
y_plus_epsilon = -1 + 1e-10
t_stop = 10
# Here if I use my N=72 The graph look ugly, so I used N=100000
# If I use N=72 the graph looks like 2 streight lines.
N=100000
h = (t_stop - t_start) / N

t, y = rk_4_for_problem3(f, y_plus_epsilon, t_start, t_stop, h)
print(f"Stuck at y = 0 between {round(t[1], 3)} and {round(t[-1], 5)}")

#Plot - I wanted to make it nice...
plt.figure(figsize=(10, 6))
plt.title('Graph of y against t')
plt.plot(t, y, color='blue', linestyle='-', linewidth=2, label='y vs. t for N=100000')

# Add horizontal lines for zero & tolerance
plt.axhline(0, color='gray', linestyle='--')
plt.axhline(1e-4, color='red', linestyle='--', label="y=10^-4")
plt.axhline(-1e-4, color='red', linestyle='--', label="y=-10^-4")

plt.xlabel('t')
plt.ylabel('y')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()


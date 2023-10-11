import math 
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 30

def get_negative(value):
    return -Decimal(value)

def compute_pi_approximation(step_size):
    step_size = Decimal(f"{step_size}")
    
    # Initial values    
    current_y, derivative_y, current_x = Decimal(1), Decimal(0), Decimal(0)
    
    while True:
        
        # Compute the k values for y and n values for derivative_y
        k1 = step_size * derivative_y
        n1 = step_size * get_negative(current_y)
        k2 = step_size * (derivative_y + Decimal(0.5) * n1)
        n2 = step_size * get_negative(current_y + Decimal(0.5) * k1)
        k3 = step_size * (derivative_y + Decimal(0.5) * n2)
        n3 = step_size * get_negative(current_y + Decimal(0.5) * k2)
        k4 = step_size * (derivative_y + n3)
        n4 = step_size * get_negative(current_y + k3)  

        # Update current_y, derivative_y, and current_x values
        current_y += (Decimal(1)/Decimal(6)) * (k1 + 2*k2 + 2*k3 + k4)
        derivative_y += (Decimal(1)/Decimal(6)) * (n1 + 2*n2 + 2*n3 + n4)
        current_x += step_size
        
        # Exit condition: when current_y crosses zero
        if current_y <= Decimal("0"):
            previous_x = current_x - step_size
            previous_y = current_y - (Decimal(1)/Decimal(6))*(k1 + 2*k2 + 2*k3 + k4)
            break
            
    return previous_x, current_x, previous_y, current_y

def correct_decimal_places(true_value, estimated_value):
    for i, (actual, estimated) in enumerate(zip(str(true_value)[2:], str(estimated_value)[2:])):
        if actual != estimated:
            return i
    return i + 1

def get_pi_approximation(step_size):
    prev_x, curr_x, prev_y, curr_y = compute_pi_approximation(step_size)
    pi_estimate = prev_x - prev_y * (curr_x - prev_x) / (curr_y - prev_y)
    pi_estimate *= 2
    
    actual_pi = Decimal("3.141592653589793238462643")
    decimals_correct = correct_decimal_places(actual_pi, pi_estimate)
    
    print(f"Estimated value of pi:   {pi_estimate}")
    print(f"Actual value of pi:      {actual_pi}")
    print(f"Correct decimal places:  {decimals_correct}")

get_pi_approximation(1e-7)
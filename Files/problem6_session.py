import numpy as np
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 28

def dydx_function(x, y):
    return np.array([y[1], -y[0]])

def runge_kutta_method(dydx, initial_y, initial_x, step_size):
    step_size = Decimal(step_size)
    current_y = initial_y
    current_x = initial_x

    while True:
        k1 = dydx(current_x, current_y)
        k2 = dydx(current_x + step_size / 2, current_y + step_size / 2 * k1)
        k3 = dydx(current_x + step_size / 2, current_y + step_size / 2 * k2)
        k4 = dydx(current_x + step_size, current_y + step_size * k3)
        
        next_y = current_y + step_size / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        next_x = current_x + step_size

        if next_y[0] < 0:
            return [current_x, next_x], [current_y, next_y]

        current_y = next_y
        current_x = next_x

def correct_decimal_places(true_value, estimate):
    true_str = str(true_value)
    estimate_str = str(estimate)

    correct_decimals = 0
    for t, e in zip(true_str.split('.')[1], estimate_str.split('.')[1]):
        if t == e:
            correct_decimals += 1
        else:
            break
    return correct_decimals

initial_conditions = np.array([Decimal(1), Decimal(0)]).T
start_time = 0
step_size = 1e-8

time_values, y_values = runge_kutta_method(dydx_function, initial_conditions, start_time, step_size)

slope = (y_values[1] - y_values[0]) / (time_values[1] - time_values[0])
previous_y = y_values[-2]

half_pi_estimate = time_values[-2] - previous_y / slope
pi_estimate = 2 * half_pi_estimate

actual_pi = Decimal("3.141592653589793238462643")
decimals_correct = correct_decimal_places(actual_pi, pi_estimate)

print(f"Estimated value of pi:   {pi_estimate}")
print(f"Actual value of pi:      {actual_pi}")
print(f"Correct decimal places:  {decimals_correct}")
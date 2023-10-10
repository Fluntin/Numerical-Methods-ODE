import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITATIONAL_CONSTANT = 39
MASS_SUN = 1
MASS_EARTH = 1/332946
MASS_JUPITER = 318 * MASS_EARTH
TIME_STEP = 1e-3
TIME_END = 2

# Initial Values
def initialize_values(r_initial, v_initial):
    t_values = np.arange(0, TIME_END, TIME_STEP)
    r_values, v = np.zeros((2, len(t_values))), np.array(v_initial)
    r_values[:, 0] = np.array(r_initial)
    return t_values, r_values, v

# Gravitational influence on a body due to the sun
def gravitational_influence_by_sun(x):
    return x * (-GRAVITATIONAL_CONSTANT * MASS_SUN / np.linalg.norm(x)**3)

# Gravitational influence on a probe due to all bodies
def gravitational_influence_on_probe(r, r_earth, r_jupiter):
    term_earth = (r_earth - r) * MASS_EARTH * np.power(np.linalg.norm(r - r_earth), -3)
    term_jupiter = (r_jupiter - r) * MASS_JUPITER * np.power(np.linalg.norm(r - r_jupiter), -3)
    return GRAVITATIONAL_CONSTANT * (-r * MASS_SUN / np.linalg.norm(r)**3 + term_earth + term_jupiter)

# Orbit calculation for a celestial body
def calculate_orbit(t_values, r_values, v, influence_function, *args):
    for i in range(len(t_values)-1):
        if args:  # Additional arguments are provided
            v += TIME_STEP * influence_function(r_values[:, i], i)
        else:
            v += TIME_STEP * influence_function(r_values[:, i])
        r_values[:, i+1] = r_values[:, i] + TIME_STEP * v
    return r_values

# Main
def main():
    # Earth initialization and calculation
    t_values, r_earth, v_earth = initialize_values([1, 0], [0, 6.28])
    r_earth = calculate_orbit(t_values, r_earth, v_earth, gravitational_influence_by_sun)
    
    # Jupiter initialization and calculation
    _, r_jupiter, v_jupiter = initialize_values([5.1, 0], [0, 0.44 * 6.28])
    r_jupiter = calculate_orbit(t_values, r_jupiter, v_jupiter, gravitational_influence_by_sun)
    
    # Probe initialization
    r_probe_initial = [1.001, 0]
    escape_velocity = np.sqrt(2 * GRAVITATIONAL_CONSTANT * MASS_SUN / np.linalg.norm(r_probe_initial))
    v_probe_initial = [7.589, np.sqrt((escape_velocity - 0.4)**2 - 7.589**2)]
    _, r_probe, v_probe = initialize_values(r_probe_initial, v_probe_initial)
    
    # Probe orbit calculation with gravitational influence from all celestial bodies
    influence_on_probe = lambda r, i: gravitational_influence_on_probe(r, r_earth[:, i], r_jupiter[:, i])
    r_probe = calculate_orbit(t_values, r_probe, v_probe, influence_on_probe, i)

    # Plotting
    plt.plot(r_earth[0, :], r_earth[1, :], label='Earth')SSS
    plt.plot(r_jupiter[0, :], r_jupiter[1, :], label='Jupiter')
    plt.plot(r_probe[0, :], r_probe[1, :], '--', label='Probe')WS
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

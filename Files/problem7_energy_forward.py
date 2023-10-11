import matplotlib.pyplot as plt

# Constants
GRAVITY_CONSTANT = 6.67430e-11
AU = 1.496e11 
EARTH_ORBITAL_VELOCITY = 29783.0
JUPITER_ORBITAL_VELOCITY = 13069.0
YEAR_IN_SECONDS = 365.0 * 24.0 * 3600.0

M_Sun = 1.989e30 # Mass of Sun
M_Earth = 5.972e24  # Mass of Earth
M_Jupiter = 1.898e27  # Mass of Jupiter

def gravitational_acceleration(mass, x, y):
    distance_squared = x**2 + y**2
    distance_cubed = distance_squared**(1.5)
    acceleration_x = - (GRAVITY_CONSTANT * mass * x) / distance_cubed
    acceleration_y = - (GRAVITY_CONSTANT * mass * y) / distance_cubed
    return acceleration_x, acceleration_y

def kinetic_energy(mass, vx, vy):
    return 0.5 * mass * (vx**2 + vy**2)

def potential_energy(mass1, mass2, x, y):
    r = (x**2 + y**2)**0.5
    return - GRAVITY_CONSTANT * mass1 * mass2 / r

def euler_forward_energy():
    current_time = 0
    end_time = 20 * YEAR_IN_SECONDS
    time_step = 50000

    x_earth = AU
    y_earth = 0
    x_velocity_earth = 0
    y_velocity_earth = EARTH_ORBITAL_VELOCITY

    x_jupiter = 5.2 * AU
    y_jupiter = 0
    x_velocity_jupiter = 0
    y_velocity_jupiter = JUPITER_ORBITAL_VELOCITY * 0.7

    energies_earth = []
    energies_jupiter = []
    times = []

    while current_time <= end_time:
        ax_earth, ay_earth = gravitational_acceleration(M_Sun, x_earth, y_earth)
        ax_jupiter, ay_jupiter = gravitational_acceleration(M_Sun, x_jupiter, y_jupiter)

        x_earth += time_step * x_velocity_earth
        y_earth += time_step * y_velocity_earth
        x_velocity_earth += time_step * ax_earth
        y_velocity_earth += time_step * ay_earth

        x_jupiter += time_step * x_velocity_jupiter
        y_jupiter += time_step * y_velocity_jupiter
        x_velocity_jupiter += time_step * ax_jupiter
        y_velocity_jupiter += time_step * ay_jupiter

        T_earth = kinetic_energy(M_Earth, x_velocity_earth, y_velocity_earth)
        U_earth = potential_energy(M_Earth, M_Sun, x_earth, y_earth)
        T_jupiter = kinetic_energy(M_Jupiter, x_velocity_jupiter, y_velocity_jupiter)
        U_jupiter = potential_energy(M_Jupiter, M_Sun, x_jupiter, y_jupiter)

        energies_earth.append(T_earth + U_earth)
        energies_jupiter.append(T_jupiter + U_jupiter)
        times.append(current_time)

        current_time += time_step

    return times, energies_earth, energies_jupiter

def plot_energies():
    times, energies_earth, energies_jupiter = euler_forward_energy()

    plt.figure(figsize=(12, 8))

    # Plot for Earth
    plt.subplot(2, 1, 1)
    plt.plot(times, energies_earth, label="Earth's Energy", color='blue')
    plt.xlabel('Time [s]')
    plt.ylabel('Total Energy [J]')
    plt.title("Euler Forward - Earth's Total Energy")
    plt.grid(True)
    plt.legend()

    # Plot for Jupiter
    plt.subplot(2, 1, 2) 
    plt.plot(times, energies_jupiter, label="Jupiter's Energy", color='orange')
    plt.xlabel('Time [s]')
    plt.ylabel('Total Energy [J]')
    plt.title("Euler Forward - Jupiter's Total Energy")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

plot_energies()
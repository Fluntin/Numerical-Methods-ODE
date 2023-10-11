
import math 
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

#Space Contstants
G = 6.67428e-11 # gravitational constant in m^3 kg^-1 s^-2
AU = 1496e8 # 1 AU in meters

# Gravitational force between two bodies in space
def gravitational_attraction(first_mass, second_mass):

    # First I compute the distance between the two bodies
    # We do it step by step to make the code more readable
    first_x, first_y = first_mass['position_x'], first_mass['position_y']
    second_x, second_y = second_mass['position_x'], second_mass['position_y']
    distance_x = (second_x-first_x)
    distance_y = (second_y-first_y)
    distance_total = math.sqrt(distance_x**2 + distance_y**2)

    # Then I compute the total force between the two bodies
    force_total = G * first_mass['mass'] * second_mass['mass'] / (distance_total**2)
    
    # Then I compute the force components in the x and y directions
    # I think this is what i missed before
    theta = math.atan2(distance_y, distance_x)
    force_x = math.cos(theta) * force_total
    force_y = math.sin(theta) * force_total
    return force_x, force_y

#The machine learning part
def celestial_machine(celestial_bodies):
    timestep =864e3

    #Trajectories is a dictionary of lists of x and y positions for each body
    trajectories = {body['id']: {'x': [], 'y': []} for body in celestial_bodies}

    for _ in range(365):  # simulate for one year, you can increase this if needed
        force = {}
        for object in celestial_bodies:
            total_fx = total_fy = 0.0
            
            # I think this is the part that I missed before
            for other in celestial_bodies:
                
                # This helps us avoid self interaction
                if object is other:
                    continue
                
                # At each point in time, we compute the force between the two bodies for all pairs of bodies!
                else:
                    force_x, force_y = gravitational_attraction(object, other)
                    total_fx += force_x
                    total_fy += force_y
            
            # We store the total force on each body in a dictionary for a given time step
            force[object['id']] = (total_fx, total_fy)

        for object in celestial_bodies:
            force_x, force_y = force[object['id']]
            
            # This is just Newton's second law of motion
            object['velocity_x'] += force_x / object['mass'] * timestep
            object['velocity_y'] += force_y / object['mass'] * timestep

            # This is just finding the new position using the velocity we computed above
            object['position_x'] += object['velocity_x'] * timestep
            object['position_y'] += object['velocity_y'] * timestep

            # Now we store the positions in the dictionary
            trajectories[object['id']]['x'].append(object['position_x'])
            trajectories[object['id']]['y'].append(object['position_y'])

    # Trajectories is a dictionary of lists of x and y positions for each body
    return trajectories

import matplotlib.pyplot as plt

#Sun
M_Sun=1.98892e30 #Google
position_sun_x=0
position_sun_y=0
velocity_sun_x=0
velocity_sun_y=0

#Earth
M_Earth=5.9742e24 #Google
position_earth_x=-1*AU #Google
position_earth_y=0
velocity_earth_x=0
velocity_earth_y=29783 #Google

#Juiter
M_Jupiter=1.89813e27 #Google
position_jupiter_x=0
position_jupiter_y=3*AU #TO make it simple in realit Jupiter is 5.2*AU
velocity_jupiter_x=17020 # Guess
velocity_jupiter_y=0

#-------------------------------------------------------------------------------------------------------
#Satelit
M_Satelit=1e3 #Typically in the range of 2,000 kg to 6,000 kg. => 1e3
position_satelit_x=-1.1*AU #Arbitrary
position_satelit_y=0
velocity_satelit_x=0

# Just to demostrate how sesitive this is; 34000 works great but escape_velocity_satelit*0.80708=33999.82290871171 does not work that well...
#velocity_satelit_y=escape_velocity_satelit*0.80708  #34000
def escape_velocity(M, r):
    return np.sqrt(2*G*M/r)

escape_velocity_satelit = escape_velocity(M_Sun, AU)
print(escape_velocity_satelit*0.80708)

velocity_satelit_y=escape_velocity_satelit*0.80708 # If I change to 34000 it works better
#-------------------------------------------------------------------------------------------------------

Sun = {'id': 'Sun', 'mass': M_Sun, 'position_x': position_sun_x, 'position_y': position_sun_y, 'velocity_x': velocity_sun_x, 'velocity_y': velocity_sun_y}
Earth = {'id': 'Earth', 'mass': M_Earth, 'position_x': position_earth_x, 'position_y':  position_earth_y, 'velocity_x': velocity_earth_x, 'velocity_y': velocity_earth_y}
Jupiter = {'id': 'Jupiter', 'mass': M_Jupiter, 'position_x': position_jupiter_x, 'position_y': position_jupiter_y, 'velocity_x': velocity_jupiter_x, 'velocity_y': velocity_jupiter_y}
Satelit = {'id': 'satelit', 'mass': M_Satelit, 'position_x': position_satelit_x, 'position_y': position_satelit_y, 'velocity_x': velocity_satelit_x, 'velocity_y': velocity_satelit_y}

#-------------------------------------------------------------------------------------------------------

orbits = celestial_machine([Sun, Earth, Jupiter, Satelit])

#-------------------------------------------------------------------------------------------------------
# Plotting
# Define a color map for the bodies
color_map = {
    'Sun': 'gold',
    'Earth': 'royalblue',
    'Jupiter': 'darkorange',
    'satelit': 'gray'
}

# Increase the size of the figure
plt.figure(figsize=(10, 10))

# Use a different style
plt.style.use('seaborn-darkgrid')


for body, trajectory in orbits.items():
    plt.plot(trajectory['x'], trajectory['y'], label=body, color=color_map[body], linewidth=2)

plt.xlabel('Distance in X direction [m]')
plt.ylabel('Distance in Y direction [m]')
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True)
plt.title('Gravitational Sling')
plt.show()
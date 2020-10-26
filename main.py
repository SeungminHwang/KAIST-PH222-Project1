import csv
import numpy as np
import matplotlib.pyplot as plt

from src.fileIO import *
from src.SolarSystemObj import *
from src.Spacecraft import *


# global variables for simulation
global_time = 0
time_unit = 60*60 # unit time in seconds
dt = time_unit
time_max = 43824 # modify
t0 = 583


# load planetary motion data from 200701 ~ 250701
sun_x, sun_y, sun_z, sun_vx, sun_vy, sun_vz = load_data('data/sun_position_200701_250701.csv')
earth_x, earth_y, earth_z, earth_vx, earth_vy, earth_vz = load_data('data/earth_position_200701_250701.csv')
mars_x, mars_y, mars_z, mars_vx, mars_vy, mars_vz = load_data('data/mars_position_200701_250701.csv')

# Sun, Earth and Mars
Earth = SolarSystemObj(earth_x, earth_y, earth_z, earth_vx, earth_vy, earth_vz, 
                       m = 5.97219e24, GM = 398600.435436)
Mars = SolarSystemObj(mars_x, mars_y, mars_z, mars_vx, mars_vy, mars_vz, 
                      m = 6.4171e24, GM = 42828.375214)
Sun = SolarSystemObj(sun_x, sun_y, sun_z, sun_vx, sun_vy, sun_vz, 
                     m = 1988500e24, GM = 132712440041.93938)




## Program usage example

# Spacecraft
a, b, c = Earth.pos
d, e, f = Earth.vel
Neopjuk = Spacecraft(a, b, c, d, e, f, m = 1000, dt = dt)
'''
Neopjuk = Spacecraft(2.366316477099450E+07, -1.492958432218654E+08,  4.003855446992815E+04,
                     2.962261494811474E+01,  3.968675665909877E+00, -6.854732365598415E-02,
                     m = 7.349e22,
                     dt = dt)
'''


# What object will be considered in the numerical calculation
object_list = [Mars, Sun]


# lists for plot
x_list = []
y_list = []
z_list = []

# simulation start
for t in range(time_max):
    x, y, z = Neopjuk.pos
    
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)    
    
    if(t > t0):
        Neopjuk.acceleration(object_list)
        Neopjuk.update()
        
    # final update(state transition: positions, velocities)
    for obj in object_list:
        obj.update(t + 1)
        



# plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = len(x_list)

ax.plot(x_list[:n], y_list[:n], z_list[:n], label="Simulated Moon")
ax.plot(earth_x[:n], earth_y[:n], earth_z[:n], label= "Earth")


ax.set_xlabel("km")
ax.set_ylabel("km")
ax.set_zlabel("km")
ax.legend()


plt.show()



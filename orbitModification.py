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
time_max = 40000 # modify
t0 = 19044

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




# Spacecraft
a, b, c = earth_x[t0], earth_y[t0], earth_z[t0]
d, e, f = earth_vx[t0], earth_vy[t0], earth_vz[t0]

center_earth_x = -595077.316945
center_earth_y = -2389581.397178

center_mars_x = -20594013.960874
center_mars_y = 8575697.237335


tangent_vel = 2.9392965764624415 * 1.17
tangent_dir = np.array([-(b - center_earth_y), (a - center_earth_x)])
tangent_vec = tangent_vel*tangent_dir/np.linalg.norm(tangent_dir)
#d, e = 
print(a, b, c, d, e, f)# - tangent_vec)
print(tangent_vec)


#Neopjuk = Spacecraft(a, b, c, d, e, f, m = 1, dt=dt)

Neopjuk = Spacecraft(1.402143470545298E+08, -5.218328737471491E+07,  3.211646647775546E+04,
                     9.838386925041595E+00 + tangent_vec[0],  2.781752062424732E+01 + tangent_vec[1], -2.172883230144862E-04 + 6.2,
                     m = 1,
                     dt = dt)



# What object will be considered in the numerical calculation
object_list = [Sun, Mars]


# lists for plot
x_list = []
y_list = []
z_list = []

# simulation start
for t in range(t0, time_max):
    x, y, z = Neopjuk.pos

    x_list.append(x)
    y_list.append(y)
    z_list.append(z)    

    Neopjuk.acceleration(object_list)
    # final update(state transition: positions, velocities)
    for obj in object_list:
        obj.update(t + 1)
    
    Neopjuk.update()
    if(t == t0 + 6753): # sudden accel.
        vx, vy, vz = Neopjuk.vel
        
        tangent_vel = 2.6448508875120633 * 0.82
        tangent_dir = np.array([-(Mars.pos[1] - center_mars_y), (Mars.pos[0] - center_mars_x)])
        tangent_vec = tangent_vel*tangent_dir/np.linalg.norm(tangent_dir)
        
        Neopjuk.update_v_force(vx + tangent_vec[0], vy + tangent_vec[1], vz + 3.25)



# plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#n = t0 + 6685 + 1000#len(x_list)
n = 40000#len(x_list)

ax.plot(x_list[:n], y_list[:n], z_list[:n], label="Spacecraft")
ax.plot(x_list[0], y_list[0], z_list[0], 'o', markersize=4, label="Ei")
ax.plot(x_list[6753], y_list[6753], z_list[6753], 'o', markersize=4, label="Sf")
ax.plot(mars_x[t0 + 6753], mars_y[t0 + 6753], mars_z[t0 + 6753], 'o', markersize=4, label= "M_f")
ax.plot(earth_x[:n], earth_y[:n], earth_z[:n], label= "Earth")
ax.plot(mars_x[:n], mars_y[:n], mars_z[:n], label= "mars")


ax.set_xlabel("km")
ax.set_ylabel("km")
ax.set_zlabel("km")
ax.legend()


plt.show()

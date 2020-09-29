import csv
import numpy as np
from fileIO import *

import matplotlib.pyplot as plt

dt = 60*60

class SolarSystemObj():
    def __init__(self, x, y, z, vx, vy, vz, m, GM):
        self.pos_list = (x, y, z)
        self.vel_list = (vx, vy, vz)
        self.mass = m
        self.GM = GM # in km^3/s^2
        
        # vectors(position, velocity)
        self.pos = np.array((x[0], y[0], z[0])) # position at t = T, initially r(t = 0)
        self.vel = np.array((vx[0], vy[0], vz[0])) # position at T = T, initially v(t = 0)
    
    def position(self, t):
        x = self.pos[0][t]
        y = self.pos[1][t]
        z = self.pos[2][t]
        
        return np.array((x, y, z))
        
    def veloity(self, t):
        vx = self.vel[0][t]
        vy = self.vel[1][t]
        vz = self.vel[2][t]
        
        return np.array((vx, vy, vz))
    
    def update(self, t):
        self.pos = (self.pos_list[0][t], self.pos_list[1][t], self.pos_list[2][t])
        self.vel = (self.vel_list[0][t], self.vel_list[1][t], self.vel_list[2][t])




class Spacecraft():
    def __init__(self, x, y, z, vx, vy, vz, m):
        self.pos_list = ([x], [y], [z])
        self.vel_list = ([vx], [vy], [vz])
        self.mass = m
        
        self.pos = np.array((x, y, z))
        self.vel = np.array((vx, vy, vz))
        self.a = np.array((0, 0, 0)) # this is dummy value
    
    def displacement(self, obj): # direction spacecraft -> solar system object
        return obj.pos - self.pos
    
    def acceleration(self, obj_list):
        a = 0.0
        for obj in obj_list:
            r = self.displacement(obj) # displacement vector
            r_mag = np.linalg.norm(r) # norm of r
            
            
            # accel.: weird calculation order for preventing better float point calculation
            a += (obj.GM/r_mag)*(r/r_mag)/r_mag
        self.a = a
        
        return a
        
    def update(self):
        # By using pseudo-uniformly-accelerated motion
        next_pos = self.pos + self.vel*dt + 0.5*self.a*dt*dt # get next position
        next_vel = self.vel + self.a*dt # get next velocity
        
        
        # transition to next_state
        self.pos = next_pos
        self.vel = next_vel






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
a, b, c = Earth.pos
d, e, f = Earth.vel
#Neopjuk = Spacecraft(a + 6400, b, c, d, e, f, m = 1000)
Neopjuk = Spacecraft(2.366316477099450E+07, -1.492958432218654E+08,  4.003855446992815E+04,
                     2.962261494811474E+01,  3.968675665909877E+00, -6.854732365598415E-02,
                     m = 7.349e22)




# global variables for simulation
global_time = 0
time_unit = 60*60 # unit time in seconds
time_max = len(sun_x) - 1 # modify



# What object will be considered in the numerical 
object_list = [Earth, Mars, Sun]


# simulation
x_list = []
y_list = []
z_list = []
for t in range(365*24*1):#time_max):
    x, y, z = Neopjuk.pos
    
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)    
    
    Neopjuk.acceleration(object_list)
    # final update(state transition: positions, velocities)
    for obj in object_list:
        obj.update(t + 1)
    Neopjuk.update()
    
    
    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot(x_list, y_list, z_list, label="Simulated Moon")
ax.plot(earth_x, earth_y, earth_z, label= "Earth")


ax.set_xlabel("km")
ax.set_ylabel("km")
ax.set_zlabel("km")
ax.legend()


plt.show()





# circular orbit 



import numpy as np
import matplotlib.pyplot as plt

from src.fileIO import *
from src.circularOrbitRegression import *





# load planetary motion data from 200701 ~ 250701
sun_x, sun_y, sun_z, sun_vx, sun_vy, sun_vz = load_data('data/sun_position_200701_250701.csv')
earth_x, earth_y, earth_z, earth_vx, earth_vy, earth_vz = load_data('data/earth_position_200701_250701.csv')
mars_x, mars_y, mars_z, mars_vx, mars_vy, mars_vz = load_data('data/mars_position_200701_250701.csv')
mars2020_x, mars2020_y, mars2020_z, mars2020_vx, mars2020_vy, mars2020_vz = load_data('data/MARS2020_position_200731_210220.csv')


# Best-fit circular orbit
a_e, b_e, c_e = -595077.316945, -2389581.397178, 149592959.712259
a_m, b_m, c_m = -20594013.960874, 8575697.237335, 227414505.970711


# total number of position data
num_data = len(sun_x)

# d = Center_E - Center_M 
d_vec = np.array([a_e - a_m, b_e - b_m])

center_Earth = np.array([a_e, b_e])
center_Mars = np.array([a_m, b_m])


# temp
destx_list = []
desty_list = []
a_list = []
t_list = []

for i in range(num_data):
    
    # position vector
    pos_Earth = np.array([earth_x[i], earth_y[i]])
    post_Mars = np.array([mars_x[i], mars_y[i]])
    
    R_e_vec = pos_Earth - center_Earth
    R_m_vec = post_Mars - center_Mars
    
    # values
    d = np.linalg.norm(d_vec) # d (scalar)
    R_e = np.linalg.norm(R_e_vec) # R_E (scalar)
    R_m = np.linalg.norm(R_m_vec) # R_M (scalar)
    
    
    d_cos_theta = d * np.sum(R_e_vec*d_vec)/(R_e*d)
    
    
    # Semi-major axis of transfer orbit
    a = 0.5*R_e + 0.5*d_cos_theta + 0.5*np.sqrt(d_cos_theta*d_cos_theta + R_m*R_m - d*d)
    
    
    time_transfer = (np.pi/np.sqrt(132712440041.93938))*np.sqrt(a*a*a)
    t_list.append(time_transfer)
    
    if( i % 170 == 1):
        dest = pos_Earth - 2*a*(R_e_vec/R_e)
        destx_list.append(dest[0])
        desty_list.append(dest[1])


plt.plot(t_list)
plt.show()

# Visualization
fig, ax = plt.subplots()
w = 10
h = 10
fig.set_size_inches(w,h)


t = np.linspace(0, 2*np.pi, 100)
ax.plot(c_e*np.cos(t) + a_e, c_e*np.sin(t) + b_e, label="circular Earth", marker = 'o', markersize = 4)
ax.plot(a_e,b_e, 'o', markersize=10, label='Center of Earth')

ax.plot(c_m*np.cos(t) + a_m, c_m*np.sin(t) + b_m, label="circular Mars", marker = 'o', markersize = 4)
ax.plot(a_m,b_m, 'o', markersize=10, label='Center of Mars')


#ax.plot(earth_x, earth_y, label="Earth's Orbit")
#ax.plot(mars_x, mars_y, label="Mars's Orbit")
ax.plot(sun_x, sun_y ,'o', label="Sun")
#ax.plot(mars2020_x, mars2020_y,'o', markersize=4, label="Mars2020's Orbit")


ax.plot(destx_list, desty_list,'o', markersize = 4, label= "aphelion of transfer orbit")




ax.legend(loc="upper right", fontsize = 20)
plt.show()


# circular orbit 



import numpy as np
import matplotlib.pyplot as plt

from src.fileIO import *
from src.circularOrbitRegression import *





# load planetary motion data from 200701 ~ 250701
sun_x, sun_y, sun_z, sun_vx, sun_vy, sun_vz = load_data('data/sun_position_200701_250701.csv')
earth_x, earth_y, earth_z, earth_vx, earth_vy, earth_vz = load_data('data/earth_position_200701_250701.csv')
mars_x, mars_y, mars_z, mars_vx, mars_vy, mars_vz = load_data('data/mars_position_200701_250701.csv')


# projection
pos_earth = [earth_x, earth_y]
pos_mars = [mars_x, mars_y]


a_e, b_e, c_e = findBestFitCircle(earth_x, earth_y, c0 = 1.5e8)
a_m, b_m, c_m = findBestFitCircle(mars_x, mars_y, c0 = 2e8)




fig, ax = plt.subplots()
w = 10
h = 10
fig.set_size_inches(w,h)


t = np.linspace(0, 2*np.pi, 100)
ax.plot(c_e*np.cos(t) + a_e, c_e*np.sin(t) + b_e, label="circular Earth", marker = 'o', markersize = 4)
ax.plot(a_e,b_e, 'o', markersize=10, label='Center of Earth')

ax.plot(c_m*np.cos(t) + a_m, c_m*np.sin(t) + b_m, label="circular Mars", marker = 'o', markersize = 4)
ax.plot(a_m,b_m, 'o', markersize=10, label='Center of Mars')


ax.plot(earth_x, earth_y, label="Earth's Orbit")
ax.plot(mars_x, mars_y, label="Mars's Orbit")


ax.plot(earth_x[700 + 8760], earth_y[700 + 8760], 'o', markersize=10, label="ei")
ax.plot(mars_x[700 + 8760], mars_y[700 + 8760], 'o', markersize=10, label="mi")

ax.plot(earth_x[5600 + 8760], earth_y[5600 + 8760], 'o', markersize=10, label="ef")
ax.plot(mars_x[5600 + 8760], mars_y[5600 + 8760], 'o', markersize=10, label="mf")

ax.plot(earth_x[5600 + 8760 + 5040], earth_y[5600 + 8760 + 5040], 'o', markersize=10)
ax.plot(mars_x[5600 + 8760 + 5040], mars_y[5600 + 8760 + 5040], 'o', markersize=10)



ax.legend(loc="upper right")
plt.show()


# Orbit plot in 3D


import csv
import numpy as np

import matplotlib.pyplot as plt # for visualization
from mpl_toolkits.mplot3d import Axes3D


def load_data(file_name):
    # For return values
    
    x_list = []
    y_list = []
    z_list = []
    
    vx_list = []
    vy_list = []
    vz_list = []
    
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar="'")
        
        next(reader) # skip the first line of the table
        
        for row in reader:
            _, date_time, x, y, z, vx, vy, vz, _ = row
            
            x_list.append(float(x))
            y_list.append(float(y))
            z_list.append(float(z))
        
        
    return x_list, y_list, z_list


# Sun, Earth and Mars
sun_x, sun_y, sun_z = load_data('data/sun_position_200701_250701.csv')
earth_x, earth_y, earth_z = load_data('data/earth_position_200701_250701.csv')
mars_x, mars_y, mars_z = load_data('data/mars_position_200701_250701.csv')



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot(sun_x, sun_y, sun_z, label="Sun")
ax.plot(earth_x, earth_y, earth_z, label="Earth")
ax.plot(mars_x, mars_y, mars_z, label="Mars")


ax.set_xlabel("km")
ax.set_ylabel("km")
ax.set_zlabel("km")
ax.legend()


plt.savefig('figures/orbits_in_3d.png', dpi=600)
plt.show()















import csv
import numpy as np


'''
def load_data(file_name);
Load NASA hoizons data into the list

# Examples
sun_x, sun_y, sun_z, sun_vx, sun_vy, sun_vz = load_data('data/sun_position_200701_250701.csv')
earth_x, earth_y, earth_z, earth_vx, earth_vy, earth_vz = load_data('data/earth_position_200701_250701.csv')
mars_x, mars_y, mars_z, mars_vx, mars_vy, mars_vz = load_data('data/mars_position_200701_250701.csv')
'''
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
            
            vx_list.append(float(x))
            vy_list.append(float(y))
            vz_list.append(float(z))

    return np.array(x_list), np.array(y_list), np.array(z_list), np.array(vx_list), np.array(vy_list), np.array(vz_list)


'''
def load_time(file_name = 'data/sun_position_200701_250701.csv'):
    
    # For return values
    time_list = []
    
    
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar="'")
        
        next(reader) # skip the first line of the table
        
        for row in reader:
            _, date_time, _, _, _, _, _, _, _ = row

            t = 1
            time_list.append(t)
            print(date_time)

    return time_list
'''
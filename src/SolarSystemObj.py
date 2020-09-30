import numpy as np

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
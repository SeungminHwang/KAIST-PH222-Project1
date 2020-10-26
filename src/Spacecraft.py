import numpy as np

class Spacecraft():
    def __init__(self, x, y, z, vx, vy, vz, m, dt):
        self.pos_list = ([x], [y], [z])
        self.vel_list = ([vx], [vy], [vz])
        self.mass = m
        
        self.pos = np.array((x, y, z))
        self.vel = np.array((vx, vy, vz))
        self.a = np.array((0, 0, 0)) # this is dummy value
        
        self.dt = dt # unit time
    
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
        next_pos = self.pos + self.vel*self.dt + 0.5*self.a*self.dt*self.dt # get next position
        next_vel = self.vel + self.a*self.dt # get next velocity
        
        
        # transition to next_state
        self.pos = next_pos
        self.vel = next_vel
    def update_v_force(self, vx, vy, vz):
        self.vel = np.array([vx, vy, vz])
        

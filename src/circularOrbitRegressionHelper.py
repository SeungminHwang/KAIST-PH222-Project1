import numpy as np

def euclidean_dist(x, y, a, b):
    nx = x - a
    ny = y - b
    
    nx_sq = nx*nx
    ny_sq = ny*ny
    
    dist_sq = nx_sq + ny_sq
    
    
    return np.sqrt(dist_sq)
    
    

def loss_func (x, y, a, b, c):
    d = euclidean_dist(x, y, a, b)
    loss = np.square(d - c)    
    return np.mean(loss)


def grad_loss (x, y, a, b, c):
    
    d1 = c
    d2 = euclidean_dist(x, y, a, b)
    
    Delta_d = d2 - d1
    
    
    dLdc = -np.mean(Delta_d)
    dLda = -np.mean(Delta_d*(x - a)/(d2))
    dLdb = -np.mean(Delta_d*(y - b)/(d2))
    
    return dLda, dLdb, dLdc

def get_next(x, y, a, b, c, step_size = 1e-8):
    grad_a, grad_b, grad_c = grad_loss(x, y, a, b, c)
    
    next_a = a - grad_a*step_size
    next_b = b - grad_b*step_size
    next_c = c - grad_c*step_size
    
    return next_a, next_b, next_c

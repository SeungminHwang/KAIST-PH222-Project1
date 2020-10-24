# regression.py
import numpy as np
from src.circularOrbitRegressionHelper import *

def findBestFitCircle(x, y, a0 = 0, b0 = 0, c0 = 149620866.996605, iter_cnt = 10000):
    a = a0
    b = b0
    c = c0
    
    step = 1e-2
    
    for i in range(iter_cnt):
        a, b, c = get_next(x, y, a, b, c, step_size=step)
        l = loss_func(x, y, a, b, c)
        if i % 1000 == 0:
            print("Epoch: %d, a = %f, b = %f, c = %f, loss = %f" %(i + 1, a, b, c, l))
            print("Grad(L): (%f %f %f)" % (grad_loss(x, y, a, b, c)))
    
    return a, b, c


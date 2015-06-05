import numpy as np
import scipy
import matplotlib.pyplot as plt 
import sys

def compute_r_squared(data,predictions):
	#SUM (predicted - average y)^2/
	#SUM (data - average y) ^2
	boven = np.square(data-predictions)
    sumBoven = np.sum(boven)
    
    onder = np.square(data-np.mean(data))
    sumOnder = np.sum(onder)
    
    divide = sumBoven/sumOnder
    r_squared  =  1 - divide
    #return r_squared
    return r_squared
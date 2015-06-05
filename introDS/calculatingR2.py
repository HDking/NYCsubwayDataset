import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # don't forget.. ** <- python way of power of u
    # YOUR CODE GOES HERE
    boven = np.square(data-predictions)
    sumBoven = np.sum(boven)
    
    onder = np.square(data-np.mean(data))
    sumOnder = np.sum(onder)
    
    divide = sumBoven/sumOnder
    r_squared  =  1 - divide
    #return r_squared
    return r_squared
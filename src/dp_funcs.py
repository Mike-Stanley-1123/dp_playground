'''
Author: Mike Stanley
Created on: September 14, 2018

Script containing functions used for exploring properties of 
dirichlet processes
'''

import numpy as np

def empirical_cdf(data):
    '''
    given data sampled from some density, return the empirical
    cdf to be plotted
    retuns an nX2 array, first column contains the data values (sorted), 
    the second column contains the cumsum pieces
    '''
    # find the x values
    x_s = np.sort(data)
    
    # find the incremental y values
    y_s = np.cumsum(np.ones(len(x_s)) / len(x_s))
    
    return np.column_stack([x_s, y_s])
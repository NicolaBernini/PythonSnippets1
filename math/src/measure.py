
import numpy as np 

def do_measure_unnormalized(in_domain): 
    return np.full(len(in_domain), 1)

def do_measure_normalized(in_domain): 
    return np.full(len(in_domain), 1/len(in_domain))


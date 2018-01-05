
import numpy as np 
import integrals 

# Kullback Leibler Divergence 
def do_kl_compute(in_p, in_q, in_domain, in_prior=None): 
    return do_expected_value( lambda x: in_p(x)*np.log(in_p(x)/in_q(x)), in_domain, in_prior )


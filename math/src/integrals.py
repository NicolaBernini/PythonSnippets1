
# The 1D Integral 
def do_integrate_1d(in_f, in_domain, in_measure=None): 
    if(in_measure==None): 
        in_measure = np.full(len(in_domain), 1/len(in_domain))
    temp=0
    for i in range(0, len(in_domain)): 
        temp += in_f(in_domain[i])*in_measure[i]
    return temp


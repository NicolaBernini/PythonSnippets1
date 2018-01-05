
# Each PDF is returned as a callable object to be evaluated 

def f_gaussian(mu, sig):
    return lambda x: np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


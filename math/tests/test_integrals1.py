
import integrals 

t_dom1 = np.arange(10)
def f_x2(x): return x^2
print("Integral Result = " + str(integrals.do_integrate_1d(f_x2, t_dom1)))

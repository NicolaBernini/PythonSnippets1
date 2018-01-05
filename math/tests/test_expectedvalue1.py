
import integrals 

t_dom1 = np.arange(10)
def f_x2(x): return x^2
print("Expected Value Result = " + str(do_expected_value(f_x2, t_dom1)))

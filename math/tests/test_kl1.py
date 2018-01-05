
import numpy as np
import infortmation_theory as it
import pdf 

# Domain 
t_dom11 = np.arange(-100, 100)


# PDFs 
t_g1 = pdf.f_gaussian(3, 11)
t_g2 = pdf.f_gaussian(0, 12)





# Compute KL Divergence 
print("KL Divergence = " + str(do_kl_compute(t_g2, t_g1, t_dom11)))

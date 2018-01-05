
import kf1 

# Prediction
t_mu_pred = np.array([0,0,0])
t_sigma_pred = np.array([0.1, 0.1, 0.2])

# Observation
t_mu_obs = np.array([0.1,0.2,0.3])
t_sigma_obs = np.array([0.5, 0.5, 0.5])







# KF Fusion 
t_mu_updated = kkf1.do_fuse_kalman1(t_mu_pred, t_sigma_pred, t_mu_obs, t_sigma_obs)


print("Updated Position = " + str(t_mu_updated))



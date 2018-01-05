
# Assumptions: Both in the same space and No Covariance 
def do_fuse_kalman1(in_mu_pred, in_sigma_pred, in_mu_obs, in_sigma_obs): 
    # Residual = Observation - Prediction 
    t_residuals = np.subtract(in_mu_obs, in_mu_pred)
    t_kalman_gains = np.divide(in_sigma_pred, np.add(in_sigma_pred, in_sigma_obs))
    
    # Posterior Mean  
    t_mu_out = np.add(in_mu_pred, np.multiply(t_residuals, t_kalman_gains))
    
    t_sigma_out = np.subtract( in_sigma_pred, np.multiply(t_kalman_gains, in_sigma_pred) )
    return t_mu_out, t_sigma_out










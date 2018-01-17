import numpy as np
#beta_nw = 0.13
#beta_se = 0.08

beta_se = 2.03178837 # u_r
beta_nw = 3.37890234 # u_a

beta_se = 0.08 # u_r
beta_nw = 0.13 # u_a

beta_se_err = 0.24166092
beta_nw_err = 0.70256672



# assume theta = 0
beta_min = (beta_nw-beta_se)/(beta_nw+beta_se)
# error prop.
beta_min_err = np.sqrt( (((2*beta_se)/(beta_nw+beta_se)**2)**2)*(beta_nw_err**2)+\
					(((-2*beta_nw)/(beta_nw+beta_se)**2)**2)*(beta_se_err**2) )
print beta_min,'+/-',beta_min_err

# assume max speed beta=1
theta_max = np.arccos((beta_nw-beta_se)/(beta_nw+beta_se))*180/np.pi
#error prop.
theta_max_err = np.sqrt((1/(1-beta_min**2))*beta_min_err**2)*180/np.pi

print theta_max,'+/-',theta_max_err




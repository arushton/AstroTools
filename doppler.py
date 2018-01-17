import numpy as np

""" A method to calculate the minimum speed or max angle (to line_of-sight)
    for a particle that has been observed to produce relativistic beaming:
    https://en.wikipedia.org/wiki/Relativistic_beaming

    By Anthony Rushton http://arushton.github.io
"""

class doppler:
    def __init__(self,*args):
        self.beta_rec = args[0]
        self.beta_app = args[1]
        self.beta_rec_err = args[2]
        self.beta_app_err  = args[3]
        self.calculate_beta_min()
        self.calculate_theta_max()

    def calculate_beta_min(self):        
        # this assumes theta = 0
        self.beta_min = (self.beta_app-self.beta_rec)/(self.beta_app+self.beta_rec)
        # error prop.
        self.beta_min_err = np.sqrt( (((2*self.beta_rec)/(self.beta_app+self.beta_rec)**2)**2)*(self.beta_app_err**2)+\
        					(((-2*self.beta_app)/(self.beta_app+self.beta_rec)**2)**2)*(self.beta_rec_err**2) )

    def calculate_theta_max(self):
        # assume max speed beta=1
        self.theta_max = np.arccos((self.beta_app-self.beta_rec)/(self.beta_app+self.beta_rec))*180/np.pi
        # error prop.
        self.theta_max_err = np.sqrt((1/(1-self.beta_min**2))*self.beta_min_err**2)*180/np.pi
        

def example():
    
    beta_se = 0.08 # u_r
    beta_nw = 0.13 # u_a
    
    beta_se_err = 0.24166092
    beta_nw_err = 0.70256672
       
    beaming = doppler(beta_se,beta_nw,beta_se_err,beta_nw_err)        
    
    
    print (beaming.beta_min,'+/-',beaming.beta_min_err)
    print (beaming.theta_max,'+/-',beaming.theta_max_err)

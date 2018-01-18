import numpy as np
from scipy import asarray as ar,exp

""" A method to calculate the intrinic properties of a sphere of relativistic 
    plasma using a known:
        observing freq
        observed flux
        spectral index
        cutoff synchrontron range
        distance
        resolved size on sky
        eta
             
    By Anthony Rushton http://arushton.github.io
"""

class plasma():
    
    # constants
    kpc = 3.08567758e19 # metres
    c = 299792458 # m/s

    def __init__(self,*args):
        # params.
        self.nu=args[0] # in Hz
        self.flux_Jy=args[1] # in Jy
        self.alpha=args[2]  # sepectral index
        self.cutoff_freq=args[3]  # spectral cut off in Hz
        self.distance=args[4]  # metres
        dist_cm=distance*1e2

        maj_deg=args[5]# size in mas
        min_deg=args[6]
        self.mean_deg=np.mean([maj_deg,min_deg])
        
        self.eta = args[7]

        self.get_volume()
        self.get_luminosity()
        self.get_min_energy()

    def get_inputs(self):
        print('\nInputs:')
        print('Obs_freq & flux density =',nu*1e-9,'GHz &',flux_Jy,'Jy')
        print('alpha =',alpha)
        print('cutoff freq range=',cutoff_freq)
        print('Distance (kpc) =',distance/kpc)
        print('Distance (km) = ',distance/1e3)
        print('Observed angular size (mas) = ',mean_deg)


    def get_volume(self):
        mean_rad = (self.mean_deg*1e-3/3600)*np.pi/180 # angle in mas to rad
        mean_size = mean_rad*self.distance*1e-3 # into km
        self.volume=(4/3)*np.pi*(1e5*mean_size/2)**3 # into cm^3
        return volume

    def get_luminosity(self):
        F = flux_Jy/((self.nu)**self.alpha)
        spec_flux = (1e-23)*F*(((1e11)**(self.alpha+1)-(1e7)**(self.alpha+1))/(self.alpha+1))
        self.luminosity = 4*np.pi*(dist_cm)**2*spec_flux
        return luminosity

    def get_min_energy(self):
        self.E_min=3.0e6*(self.eta**(4./7.))*(self.volume**(3./7.))*(self.nu**(2./7.))*(self.luminosity**(4./7.))
        self.b_min=1.8*((self.eta*self.luminosity/self.volume)**(2./7.))*(self.nu**(1./7.))
        return E_min,b_min

    def get_outputs(self):
        print('\nOutputs:')
        print('Spectral flux =',self.nu)
        print('Luminosity =',self.luminosity)
        print('Volume=',self.volume)
        print('E_min=',self.E_min)
        print('b_min =',self.b_min)


def example():
    # params. for black hole GRS1915+105
    obs_freq=8.3e9
    flux_Jy=12e-3
    alpha=-0.6
    cutoff_freq=[1e7,1e11]
    distance=2.4*kpc #metres
    dist_cm=distance*1e2    
    maj_deg=50 # size in mas
    min_deg=50
    eta = 1
    
    
    GRS1915 = plasma(obs_freq,flux_Jy,alpha,cutoff_freq,distance,maj_deg,min_deg,eta)
    GRS1915.get_inputs()
    GRS1915.get_outputs()   



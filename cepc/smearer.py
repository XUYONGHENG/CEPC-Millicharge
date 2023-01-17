import numpy as np
import tools as tool





def scale_calc(E,res1,res2=1):
    return E*np.sqrt((res1/np.sqrt(E))**2+res2**2)/100


def angular_scale_calc(E):
    return np.abs(0.024/(np.sqrt(E)) - 0.002)
# Energy smearing. Parameter E here stands for the true value of E.

def smear(E,res1=10.1,res2=0.4):
    return np.random.normal(loc=E,scale=scale_calc(E,res1,res2))


# Angular smearing. Parameter E and t stands for the true values of E and theta
def smear_angle(E,t):
    return np.random.normal(loc=t,scale=angular_scale_calc(E))


def after_smear_m(m):
    return np.random.normal(loc=m,scale=2*m*np.sqrt((m*1e-5)**2+(1e-4)**2))


# Does nothing at all. Use this as default smearer to avoid mis-smearing.
def no_smear(p):
    return p


# Designed for CEPC muon system. Only works for
def smear_angle_CEPCmu(p,radius,deltaz,deltaphi):

    # print(p)
    theta0,phi0,energy = tool.theta(p),tool.phi(p),p[0]
    # print(theta0)
    cos = np.random.normal(loc=np.cos(theta0),scale=(deltaz*(np.sin(theta0))**2/radius))
    theta = np.arccos(cos)
    if theta < 0:
        theta = np.pi
    phi = np.random.normal(loc=phi0,scale=deltaphi/radius)
    return np.array([energy,energy*np.sin(theta)*np.cos(phi),energy*np.sin(theta)*np.sin(phi),energy*np.cos(theta)])


def smear_cepc_0(p):
    # print(p)
    pp = p[:]
    phigamma = tool.phi(p[8:])

    egamma = tool.e_gamma_xx(p)
    egamma = smear(E=egamma,res1=10.1,res2=0.4)

    thetagamma = np.arccos(tool.z_gamma_xx(p))
    # cotthetagamma = 1/np.tan(thetagamma)
    # cotthetagamma = np.random.normal(loc=cotthetagamma,scale=0.063/1500)
    # thetagamma = np.arctan(1/cotthetagamma)
    # if thetagamma < 0:
    #     thetagamma = np.pi + thetagamma
    # np.arctan's out put ranges from -pi/2 to pi/2 while that of np.arccos from 0 to pi.
    # this is added to fix this trivial issue.
    pp[8:] = np.array([egamma,egamma*np.sin(thetagamma)*np.cos(phigamma),
                      egamma*np.sin(thetagamma)*np.sin(phigamma),egamma*np.cos(thetagamma)])

    return pp


def smear_cepc_mu(p):
    pp = p[:]
    phigamma = tool.phi(p[8:])

    egamma = tool.e_gamma_xx(p)
    egamma = smear(E=egamma,res1=10.1,res2=0.4)

    thetagamma = np.arccos(tool.z_gamma_xx(p))
    ppgamma = np.array([egamma,egamma*np.sin(thetagamma)*np.cos(phigamma),
                      egamma*np.sin(thetagamma)*np.sin(phigamma),egamma*np.cos(thetagamma)])

    pmu1,pmu2 = pp[:4],pp[4:8]
    ppmu1 = smear_angle_CEPCmu(p=pmu1,radius=440,deltaz=1.5,deltaphi=2)
    ppmu2 = smear_angle_CEPCmu(p=pmu2,radius=440,deltaz=1.5,deltaphi=2)

    pp[:4],pp[4:8],pp[8:] = ppmu1,ppmu2,ppgamma

    return pp


def smear_ilc(p):
    pp = p[:]
    phigamma = tool.phi(p[8:])

    egamma = tool.e_gamma_xx(p)
    egamma = smear(E=egamma,res1=16.6,res2=1.1)

    thetagamma = np.arccos(tool.z_gamma_xx(p))
    # cotthetagamma = 1/np.tan(thetagamma)
    # cotthetagamma = np.random.normal(loc=cotthetagamma,scale=0.063/1500)
    # thetagamma = np.arctan(1/cotthetagamma)
    if thetagamma < 0:
        thetagamma = np.pi + thetagamma
    # np.arctan's out put ranges from -pi/2 to pi/2 while that of np.arcos from 0 to pi.
    # this is added to fix this trivial issue.
    pp[8:] = np.array([egamma,egamma*np.sin(thetagamma)*np.cos(phigamma),
                      egamma*np.sin(thetagamma)*np.sin(phigamma),egamma*np.cos(thetagamma)])

    return pp


def smear_1307(p):
    pp = p[:]
    phigamma = tool.phi(p[8:])

    egamma = tool.e_gamma_xx(p)
    egamma = smear(E=egamma,res1=16.6,res2=1.1)

    thetagamma = np.arccos(tool.z_gamma_xx(p))
    # cotthetagamma = 1/np.tan(thetagamma)
    # cotthetagamma = np.random.normal(loc=cotthetagamma,scale=0.063/1500)
    # thetagamma = np.arctan(1/cotthetagamma)
    if thetagamma < 0:
        thetagamma = np.pi + thetagamma
    # np.arctan's out put ranges from -pi/2 to pi/2 while that of np.arcos from 0 to pi.
    # this is added to fix this trivial issue.
    pp[8:] = np.array([egamma,egamma*np.sin(thetagamma)*np.cos(phigamma),
                      egamma*np.sin(thetagamma)*np.sin(phigamma),egamma*np.cos(thetagamma)])

    return pp

if __name__ == '__main__':
    smear_cepc_mu(np.ones(shape=(12,)))
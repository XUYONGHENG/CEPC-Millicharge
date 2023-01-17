import numpy as np
import matplotlib.pyplot as plt



def exclusion(s,b,l,is_epsilon=True):
    if is_epsilon:
        a = np.sqrt(2/(s*l/np.sqrt(b*l)))*0.01
        print(a)
        return a
    else:
        return 1/np.sqrt(np.sqrt(2/(s*l/np.sqrt(b*l)))*2.5e-5)


def signal_significance(s,bg,mass,cut,dataamount=5.6e6,splusb=False,is_epsilon=True):
    print(mass,'mass')
    ssection = 0

    for i in range(s.shape[0]):
        if cut(s[i],mass):
            ssection += s[i,-1]
            # count += 1
    print(ssection,'s\n')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mass):
            bgsection += bg[i,-1]
    print(bgsection,'b\n')

    if not splusb:
        return exclusion(ssection,bgsection,dataamount,is_epsilon),ssection,bgsection
    elif splusb:
        return exclusion(ssection,bgsection+ssection,dataamount,is_epsilon),ssection,bgsection


def e_gamma_xx(p):
    return p[8]


def pt_gamma_xx(p):
    return np.sqrt(p[9]**2+p[10]**2)


def z_gamma_xx(p):
    return p[-1]/np.sqrt(p[9]**2+p[10]**2+p[11]**2)


def m_missing_xx(p):
    tmp =  (np.array([500,0,0,0])-p[8:])
    # print(tmp)
    return np.sqrt(tmp[0]**2-tmp[1]**2-tmp[2]**2-tmp[3]**2)


def m_missing_240_xx(p):
    tmp = (np.array([240,0,0,0])-2*p[8:])
    return np.sqrt(tmp[0]**2-tmp[1]**2-tmp[2]**2-tmp[3]**2)


def ivmass_xx(p,energy=240):
    tmp = (np.array([energy,0,0,0])-p[8:])
    return np.sqrt(tmp[0]**2-tmp[1]**2-tmp[2]**2-tmp[3]**2)


def theta(p):
    a =  np.arccos(p[-1]/np.sqrt(p[1]**2+p[2]**2+p[3]**2))
    if a >= 0:
        return a
    elif a < 0:
        return np.pi+a

def phi(p):
    return np.arccos(p[1]/np.sqrt(p[1]**2+p[2]**2))


def general_4_cut_applier(data,cut):
    flags = np.zeros(shape=(data.shape[0]))
    for i in range(flags.shape[0]):
        if cut(data[i]):
            flags[i] = 1
    number_of_survivors = np.int(np.sum(flags))
    survivors = np.zeros(shape=(number_of_survivors,5))
    count = 0

    for i in range(flags.shape[0]):
        if flags[i]:
            survivors[count] = data[i]
            count += 1

    return survivors,np.sum(survivors[:,-1])

def eta_to_cos(x):
    return np.cos(2*np.arctan(np.exp(-1*x)))


def gf(mz,mf,nc,c):
    # print(mz,mf,nc,c)
    return np.sqrt(mz**2-4*mf**2)*(1+2*mf**2/mz**2)/(12*np.pi)

def decay_width(mass,epsilon):
    if mass/2 < 1.28:
        w0 = epsilon**2*gf(mass,0,3,2.0/3)+2*gf(mass,0,3,-1.0/3)+2*gf(mass,0,1,-1)
    elif 1.28 <= (mass/2) <1.78:
        w0 =  epsilon**2*gf(mass,0,3,2.0/3)+2*gf(mass,0,3,-1.0/3)+2*gf(mass,0,1,-1) + gf(mass,1.28,3,2.0/3)
    elif 1.78<= (mass/2) < 4.18:
        w0 = 2*gf(mass,0,3,2.0/3)+2*gf(mass,0,3,-1.0/3)+2*gf(mass,0,1,-1) + gf(mass,1.28,3,2.0/3) + gf(mass,1.78,1,-1)
    else:
        w0 =  gf(mass,0,3,2.0/3)+2*gf(mass,0,3,-1.0/3)+2*gf(mass,0,1,-1) + gf(mass,1.28,3,2.0/3) + gf(mass,1.78,1,-1) + gf(mass,4.18,3,-1.0/3)

    return epsilon**2*w0


def total_decay_width(mzp,mx,gvx,gvf):
    if mzp <= 2* mx:
        return decay_width(mass=mzp,epsilon=gvf)

    else:
        return decay_width(mass=mzp,epsilon=gvf) + gvx **2 * gf(mz=mzp,mf=mx,nc=1,c=gvx)

def total_decay_width2(mzp,mx,gvx,gvf):
    if mzp > 2* mx:
        return (18*gvf**2*mzp+gvx**2*np.sqrt(mzp**2-4*mx**2))/(12*np.pi)
    else:
        return 18*gvf**2*mzp/(12*np.pi)





def pseudo_rapidity(p):
    return 0.5*np.log((p[8]+p[-1])/(p[8]-p[-1]))


def width_quick(gvx,gvf):
    return (18*gvf**2*150+gvx**2*np.sqrt(150**2-4*50**2))/(12*np.pi)


def pt(p):
    return np.sqrt(p[1]**2+p[2]**2)


def inner_product(p1,p2):
    return p1[0]*p2[0]-p1[1]*p2[1]-p1[2]*p2[2]-p1[3]*p2[3]


def fitsub(a,b,order):
    b0 = np.polyfit(a,b,order)
    b1 = np.poly1d(b0)
    b2 = b1(a)
    return b2


def gammaf(mzp,mf,g):
    return g**2*mzp*np.sqrt(1-4*(mf**2/mzp**2))*(1+2*(mf**2/mzp**2))**2/(12*np.pi)


def gammaf_axial(mzp,mf,g):
    return g**2*mzp*np.sqrt(1-4*(mf**2/mzp**2))*(1-4*(mf**2/mzp**2))/(12*np.pi)


def total_decay_width3(mzp,mx,gvx,gvf):
    if mzp > 2* mx:
        return 18*gvf**2*mzp/(12*np.pi) + gammaf(mzp,mx,gvx)
    else:
        return 18*gvf**2*mzp/(12*np.pi)

def total_decay_width3_axial(mzp,mx,gvx,gvf):
    if mzp > 2* mx:
        return 18*gvf**2*mzp/(12*np.pi) + gammaf_axial(mzp,mx,gvx)
    else:
        return 18*gvf**2*mzp/(12*np.pi)


# print(gammaf(150,50,1))

if __name__ == '__main__':
    # couplings = 10**np.linspace(-3,0,31)
    # print(decay_width(150,0.01))
    # print(gf(150,52,1,1))
    print(total_decay_width3(mzp=150,mx=5,gvx=1,gvf=1e-2))
    print(total_decay_width3_axial(mzp=150,mx=75,gvx=1,gvf=1e-2))
    # print(decay_width(epsilon=0.01,mass=75))
    # print(a)
    # np.save('plotformalCSV/zprime_higgsfactory_ana.npy',a)
    # a = np.zeros(shape=(100, 100, 3))
    # fig,ax = plt.figure(),plt
    # x,y = 10**np.linspace(0,-3,400),10**np.linspace(-4,-1,400)
    # # X,Y = np.meshgrid(x,y)
    # # Z = total_decay_width(mzp=150,mx=50,gvf=Y,gvx=X)
    # z = np.zeros(shape=(400,400))
    # for i in range(400):
    #     for j in range(400):
    #         z[i,j] = total_decay_width(mzp=150,mx=50,gvx=x[i],gvf=y[j])
    #         if z[i,j] > 0.5:
    #             z[i,j] = 1
    #         else:
    #             z[i,j] = 0
    # plt.imshow(z)
    # plt.show()
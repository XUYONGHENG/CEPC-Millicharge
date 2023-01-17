import numpy as np
import cut as cut
import pandas as pd


def cut_zp_v(p,mzp,mx):
    # res = m**2/1e5
    # res = 0.225
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if  (mzp-2)< p[3] < (mzp+2):
            return True

    return False


def cut_zp_iv(p,mzp,mx):
    if 95 < p[0] < 105:
        return False

    if mx<=50:
        if not (60<p[0]<85):
            return False
    else:
        if 240-p[0] < 2 * mx:
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def signal_significance_v(s,bg,mass,cut=cut_zp_v,dataamount=5e6,splusb=False,interference=False):

    ssection = 0
    # count = 0

    print(np.sum(s[:,-1]))
    for i in range(s.shape[0]):
        if cut(s[i],mzp=150,mx=mass):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    print(np.sum(bg[:,-1]))
    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mzp=150,mx=mass):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        return (((2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))**0.25)*0.01)

    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount)))








def signal_significance_iv(s,mass,bg,cut,dataamount=5e6,splusb=False,interference=False):
    ssection = 0
    # count = 0

    # s[:,-1] = 0.93*s[:,-1]
    for i in range(s.shape[0]):
        if cut(s[i],mzp=150,mx=50):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mzp=150,mx=50):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01)

    elif splusb:
        return (np.sqrt(2/(ssection*dataamount)))


if __name__ =='__main__':
    # results = np.zeros(shape=(43,))
    # masses = np.linspace(10, 200, 100)
    #
    # for i in range(43):
    #     mass = masses[i]
    #     sb = (signal_significance_wlt2(s=np.load('/store/disposed/visibledecay/dfsigm%dd.npy'%mass),bg=np.load('/store/disposed/dfbgzd.npy'),
    #                             dataamount=1.6e7,splusb=False,mass=mass
    #                                   ))
    #     print(sb)
    #     results[i] = sb
    # np.save('/store/disposed/visibledecay/resultnp2zpolev.npy',results)
    bg = np.load('/store/disposed/dfbgd.npy')
    print(np.sum(bg[:,-1]))

    # print(np.sum(np.load('/store/disposed/dfbgd.npy')[:,-1]))
    gvfs = 10**np.linspace(-3,-2,3)
    dots = np.zeros(shape=(3,2))
    for i in range(3):
        a = signal_significance_v(s=np.load('/store/disposed/couplings%d_gvf001_2d.npy'%(i+1)),
                             bg=bg,cut=cut_zp_v,splusb=False,
                             dataamount=5e6,mass=50
                             )
        dots[i] = np.array([gvfs[i],a])
    np.save('../plotformalCSV/couplings_gvffixed2.npy',dots)
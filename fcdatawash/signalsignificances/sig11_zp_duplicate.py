import numpy as np
import cut as cut
import pandas as pd


def signal_significance_v(s,bg,mass,cut=cut.cut_zp_v_150_50,dataamount=5e6,splusb=False,interference=False):

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


def signal_significance_iv(s,mx,bg,cut,dataamount=5e6,splusb=False,interference=False):
    ssection = 0

    for i in range(s.shape[0]):
        if cut(s[i],mzp=150,mx=mx):
            ssection += s[i,-1]
    print(ssection)
    print('s')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mzp=150,mx=mx):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01),np.array([ssection,bgsection])

    elif splusb:
        return (np.sqrt(2/(ssection*dataamount)))


if __name__ =='__main__':
    masses = np.linspace(50, 100, 200)
    masses = np.hstack((masses[:100],np.array([75]),masses[100:]))
    print(masses.shape)
    print(masses)
    results,xsections = np.zeros(shape=(201,2)),np.zeros(shape=(201,3))
    results[:,0],xsections[:,0] = masses,masses

    # b, a = np.load('/store/disposed/vmvmcepc3d.npy'), np.load('/store/disposed/vevecepc3d.npy')
    # b[:, -1] = 2 * b[:, -1]
    # bg = np.vstack((a, b))
    bg = np.load('/store/disposed/bg_invisibled.npy')
    tmpxsections=np.zeros(shape=(100))
    sb,xsection = (signal_significance_iv(s=np.load('/store/disposed/zp_10GeV_0.01d.npy'),
                               bg=bg,
                               dataamount=5e6, splusb=False, mx=10, cut=cut.cut_zp_iv_150_2
                               ))
    print(sb,xsection)
    print(xsection[0] * 5e6 / (np.sqrt(xsection[1] * 5e6)))
    input('halt')




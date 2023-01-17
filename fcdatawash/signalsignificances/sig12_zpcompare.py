import numpy as np
import cut as cut
import pandas as pd


def cut_zp_v(p,m):
    # res = m**2/1e5
    # res = 0.225
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if  (m-2)< p[3] < (m+2):
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


def signal_significance_v(s,bg,cut=cut_zp_v,dataamount=5e6,splusb=False,interference=False):

    ssection = 0
    # count = 0

    print(np.sum(s[:,-1]))
    for i in range(s.shape[0]):
        if cut(s[i],mass=150):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    print(np.sum(bg[:,-1]))
    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mass=150):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return (((2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))**0.5)*0.01),ssection,bgsection
        # if interference:
        #     return (ssection-bgsection)*dataamount/np.sqrt(bgsection*dataamount)
        # elif not interference:
        #     return ssection * dataamount / np.sqrt(bgsection * dataamount)
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
        # print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01)
        # if interference:
        #     return (ssection-bgsection)*dataamount/np.sqrt(bgsection*dataamount)
        # elif not interference:
        #     return ssection * dataamount / np.sqrt(bgsection * dataamount)
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
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
    masses = 10**np.linspace(0,2,51)
    b, a = np.load('/store/disposed/vmvmcepc3d.npy'), np.load('/store/disposed/vevecepc3d.npy')
    b[:, -1] = 2 * b[:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))
    for i in range(1,52):
        # print(np.sum(np.load('/store/disposed/dfbgd.npy')[:,-1]))
        a = signal_significance_iv(s=np.load('/store/disposed/cepcdfh_iv_mx_%d_run3'%i),
                             bg=bg,cut=cut_zp_iv,
                             dataamount=5e6,mass=masses[i-1]
                             )
    print(a)
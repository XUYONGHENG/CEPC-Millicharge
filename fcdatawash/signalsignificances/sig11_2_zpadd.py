import numpy as np
import cut as cut
import pandas as pd


def signal_significance_wlt(s,bg,cut=cut.cut_wlt,dataamount=5e6,splusb=False,interference=False):

    ssection = 0
    # count = 0

    print(np.sum(s[:,-1]))
    for i in range(s.shape[0]):
        if cut(s[i],mass=90):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    print(np.sum(bg[:,-1]))
    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mass=90):
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




def cut_wlt(p,m):
    # res = m**2/1e5
    # res = 0.225
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if  (m-2)< p[3] < (m+2):
            return True

    return False



def signal_significance_wlt2(s,mass,bg,dataamount=5e6,splusb=False,interference=False):

    ssection = 0
    # count = 0


    for i in range(s.shape[0]):
        if cut_wlt(s[i],m=mass):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut_wlt(bg[i],m=mass):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        # print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return ((2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))**0.5*0.01)
        # if interference:
        #     return (ssection-bgsection)*dataamount/np.sqrt(bgsection*dataamount)
        # elif not interference:
        #     return ssection * dataamount / np.sqrt(bgsection * dataamount)
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount)))


if __name__ =='__main__':
    # print(signal_significance_wlt(s=np.load('/store/disposed/zpvisible150d.npy'),bg=np.load('/store/disposed/dfbgd.npy'),
    #                         cut = cut.cut_wlt,dataamount=5e6,splusb=False
    #                               ))
    # a,b = np.load('/store/disposed/dfsigm10g0.001000d.npy'),np.load('/store/disposed/dfbgfd.npy')
    # print(np.sum(a[:,-1]),np.sum(b[:,-1]))
    # c = np.array(pd.read_csv('/store/visibledecay/fcruns/weight0.001414.dat'))
    # d = np.array(pd.read_csv('/store/visibledecay/fcruns/bgfw.dat'))
    # print(np.sum(c),np.sum(d))
    # input('halt')
    results = np.zeros(shape=(43,))
    masses = np.linspace(10, 200, 100)

    for i in range(43):
        mass = masses[i]
        sb = (signal_significance_wlt2(s=np.load('/store/disposed/dfm150g0.004419np_intd.npy'),bg=np.load('/store/disposed/dfm150g0.001250np_pured.npy'),
                                dataamount=5e6,splusb=False,mass=mass
                                      ))
        print(sb)
        results[i] = sb
    np.save('/store/disposed/visibledecay/resultnp2zpolev.npy',results)
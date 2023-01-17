import numpy as np
import cut as cut



def signal_significance_wlt(s,bg,cut=cut.cut_wlt,dataamount=5e6,splusb=False):

    ssection = 0
    # count = 0


    for i in range(s.shape[0]):
        if cut(s[i]):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i]):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        # print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return (((2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))**0.25)*0.005),ssection,bgsection
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount)))


if __name__ =='__main__':
    print(signal_significance_wlt(s=np.load('/store/disposed/wltsig5d.npy'),bg=np.load('/store/disposed/wltbgd.npy'),
                            cut = cut.cut_wlt,dataamount=5e6,splusb=False
                                  ))
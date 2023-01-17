import numpy as np
import pandas as pd
import cut as cut



# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_cepcw(s,bg,mass,cut=cut.cut_ilc_disposed_0,dataamount=5e6,splusb=False):

    ssection = 0
    # count = 0


    for i in range(s.shape[0]):
        if cut(s[i],mass):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mass):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        # print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01)
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount)))*0.01)


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    b, a = np.load('/store/disposed/milliq/cepcw/vmvmcepcwd.npy'), np.load('/store/disposed/milliq/cepcw/vevecepcwd.npy')
    print(np.sum(a[:,-1]))
    b[:, -1] = 2 * b[:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))

    # bg = np.load('/store/disposed/1211va/bgmg5d.npy')

    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dots = np.zeros(shape=(19, 2))

    dots0 = np.zeros(shape=(2,2))
    dots0[0,0],dots0[1,0] = 0.1,0.5
    dots0[0, 1] = 1e2*signal_significance_cepcw(s=np.load('/store/disposed/milliq/cepcw/mqw132m0.1d.npy'),
                                        bg=bg, mass=0.1, cut=cut.cut_cepcw_advance_disposed, dataamount=2e6,
                                        splusb=False)
    dots0[1, 1] = 1e2*signal_significance_cepcw(s=np.load('/store/disposed/milliq/cepcw/mqw132m0.5d.npy'),
                                        bg=bg, mass=0.5, cut=cut.cut_cepcw_advance_disposed, dataamount=2e6,
                                        splusb=False)


    for i in range(19):


        # Standard mq data. Generated w/ larger cut Formcalc.
        data = np.load('/store/disposed/milliq/cepcw/mqw132dot%dd.npy'%i)
        print(np.sum(data[:,-1]))
        data[:,-1] = 1e-4*data[:,-1]
        dots[i,1] = signal_significance_cepcw(s=data,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcw_advance_disposed,dataamount=2e6,splusb=False)

        dots[i,0] = masses[i]
        print(dots[i])

    dots = np.vstack((dots0,dots))
    # np.save('../plotCSV/sbdotscepcw2.npy',dots)

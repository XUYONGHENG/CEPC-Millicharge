import numpy as np
import pandas as pd
import cut as cut



# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_ilc1211(s,bg,mass,cut=cut.cut_ilc_disposed_0,dataamount=5e6,splusb=False):

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
        return np.sqrt(1/(np.sqrt(3/(ssection*dataamount/np.sqrt(bgsection*dataamount+(0.003*bgsection*dataamount)**2)))*(2.5e-5)))
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(3/(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount)))*2.5e-5)


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    a, b = np.load('/store/disposed/1211va/veveilcd.npy'), np.load('/store/disposed/1211va/vmvmilcd.npy')
    print(np.sum(a[:,-1]))
    b[:, -1] = 2 * b[:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))

    bg = np.load('/store/disposed/1211va/bgmg5d.npy')

    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dots = np.zeros(shape=(21, 2))

    for i in range(21):


        # Standard mq data. Generated w/ larger cut Formcalc.
        data = np.load('/store/disposed/1211va/dot%dd.npy'%(i+1))
        # data = np.load('/store/disposed/1211va/data%d.lhe' % (i + 1))
        print(np.sum(data[:,-1]))
        dots[i,1] = signal_significance_ilc1211(s=data,
                            bg=bg,mass=masses[i],cut=cut.cut_ilc_1211val,dataamount=2.5e5,splusb=False)

        dots[i,0] = masses[i]
        print(dots[i])

    np.save('../plotCSV/sbdotsilc1211mg5.npy',dots)

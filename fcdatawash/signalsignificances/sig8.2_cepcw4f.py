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
        return 1/np.sqrt(np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*2.5e-5)
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount)))*0.01)


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    b, a = np.load('/store/disposed/milliq/cepcw/vmvmcepcwd.npy'), np.load('/store/disposed/milliq/cepcw/vevecepcwd.npy')
    print(np.sum(a[:,-1]))
    a[:, -1] = 2 * a[:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))

    # bg = np.load('/store/disposed/1211va/bgmg5d.npy')

    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dotsvv = np.zeros(shape=(20, 2))
    dotsav = np.zeros(shape=(20, 2))
    dotsss = np.zeros(shape=(20, 2))
    dotsst = np.zeros(shape=(20, 2))

    for i in range(20):

        datass = np.load('/store/disposed/cepc4fss/cepc4fwss%dd.npy' % i)

        # Standard mq data. Generated w/ larger cut Formcalc.
        # data = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot%dd.npy'%i)
        if i <= 16:
            dataav = np.load('/store/disposed/cepc4fav/cepc4fwav%dd.npy'%i)
            datavv = np.load('/store/disposed/cepc4fvv/cepc4fwvv%dd.npy'%i)
            datast = np.load('/store/disposed/cepc4fst/cepc4fwst%dd.npy'%i)

        else:
            dataav = np.load('/store/disposed/cepc4fav/cepc4fwav%d2d.npy'%i)
            datavv = np.load('/store/disposed/cepc4fvv/cepc4fwvv%d2d.npy'%i)
            datast = np.load('/store/disposed/cepc4fst/cepc4fwst%d2d.npy'%i)
        datavv[:,-1] = 0.93*datavv[:,-1]
        dataav[:,-1] = 0.93*dataav[:,-1]
        datass[:,-1] = 0.93*datass[:,-1]
        datast[:,-1] = 0.93*datast[:,-1]

        print(np.sum(datavv[:, -1]))

        dotsvv[i,1] = signal_significance_ilc1211(s=datavv,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcw_advance_disposed_4f,dataamount=2.6e6,splusb=False)
        dotsav[i,1] = signal_significance_ilc1211(s=dataav,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcw_advance_disposed_4f,dataamount=2.6e6,splusb=False)
        dotsss[i,1] = signal_significance_ilc1211(s=datass,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcw_advance_disposed_4f,dataamount=2.6e6,splusb=False)
        dotsst[i,1] = signal_significance_ilc1211(s=datast,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcw_advance_disposed_4f,dataamount=2.6e6,splusb=False)

        dotsvv[i,0] = masses[i]
        dotsav[i,0] = masses[i]
        dotsss[i,0] = masses[i]
        dotsst[i,0] = masses[i]
        print(dotsvv[i])

    np.save('../plotformalCSV/cepcw4f/sbdotscepcw4fav.npy', dotsav)
    np.save('../plotformalCSV/cepcw4f/sbdotscepcw4fvv.npy', dotsvv)
    np.save('../plotformalCSV/cepcw4f/sbdotscepcw4fss.npy', dotsss)
    np.save('../plotformalCSV/cepcw4f/sbdotscepcw4fst.npy', dotsst)
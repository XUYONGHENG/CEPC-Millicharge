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

    b, a = np.load('/store/disposed/milliq/cepcz/vmvmcepczd.npy'), np.load('/store/disposed/milliq/cepcz/vevecepczd.npy')
    print(np.sum(a[:,-1]))
    a[:, -1] = 2*a [:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))

    # bg = np.load('/store/disposed/1211va/bgmg5d.npy')

    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dotsvv = np.zeros(shape=(17, 2))
    dotsav = np.zeros(shape=(17, 2))
    dotsss = np.zeros(shape=(17, 2))
    dotsst = np.zeros(shape=(17, 2))


    for i in range(17):

        # if i == 0 or i == 10:
        # Standard mq data. Generated w/ larger cut Formcalc.
        datast = np.load('/store/disposed/cepc4fst/cepc4fzst%dd.npy'%i)
        datass = np.load('/store/disposed/cepc4fss/cepc4fzss%dd.npy'%i)
        dataav = np.load('/store/disposed/cepc4fav/cepc4fzav%dd.npy'%i)
        datavv = np.load('/store/disposed/cepc4fvv/cepc4fzvv%dd.npy'%i)

        print(np.sum(datavv[:,-1]))

        ## ss is generated with alpha = 1/132.507 so do not apply this modifer to it.
        datast[:,-1] = (1/1.0733)*datast[:,-1]
        datass[:,-1] = (1/1.0733)*datass[:,-1]
        dataav[:,-1] = (1/1.0733)*dataav[:,-1]
        datavv[:,-1] = (1/1.0733)*datavv[:,-1]

        dotsvv[i,1] = signal_significance_ilc1211(s=datavv,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcz_advance_disposed_4f,dataamount=16e6,splusb=False)
        dotsav[i,1] = signal_significance_ilc1211(s=dataav,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcz_advance_disposed_4f,dataamount=16e6,splusb=False)
        dotsss[i,1] = signal_significance_ilc1211(s=datass,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcz_advance_disposed_4f,dataamount=16e6,splusb=False)
        dotsst[i,1] = signal_significance_ilc1211(s=datast,
                            bg=bg,mass=masses[i],cut=cut.cut_cepcz_advance_disposed_4f,dataamount=16e6,splusb=False)

        dotsvv[i,0] = masses[i]
        dotsav[i, 0] = masses[i]
        dotsss[i, 0] = masses[i]
        dotsst[i, 0] = masses[i]
        print('###############\n')
        print(i)
        print('###############\n')

    np.save('../plotformalCSV/cepcz4f/sbdotscepcz4fvv.npy',dotsvv)
    np.save('../plotformalCSV/cepcz4f/sbdotscepcz4fav.npy', dotsav)
    np.save('../plotformalCSV/cepcz4f/sbdotscepcz4fss.npy', dotsss)
    np.save('../plotformalCSV/cepcz4f/sbdotscepcz4fst.npy', dotsst)
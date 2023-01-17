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
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01),ssection,bgsection
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount)))*0.01),ssection,bgsection


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    b, a = np.load('/store/disposed/milliq/cepcz/vmvmcepczd.npy'), np.load('/store/disposed/milliq/cepcz/vevecepczd.npy')
    print(np.sum(a[:,-1]))
    b[:, -1] = 2 * b[:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))

    # bg = np.load('/store/disposed/1211va/bgmg5d.npy')

    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dots = np.zeros(shape=(16, 4))

    for i in range(16):


        # Standard mq data. Generated w/ larger cut Formcalc.
        # data = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot%dd.npy'%i)
        data = np.load('/store/disposed/darkphoton/cepcdfz%dd.npy'%i)
        # data[:,-1] = 0.93*data[:,-1]
        if i == 0:
            data[:,-1] = 0.1*data[:,-1]
        print(np.sum(data[:,-1]))
        dots[i,1:] = signal_significance_ilc1211(s=data,
                            bg=bg,mass=masses[i],cut=cut.cut_cepc_darkphoton_z,dataamount=1.6e7,splusb=False)

        dots[i,0] = masses[i]
        print(dots[i])

    np.save('../plotformalCSV/cepcdarkphoton/sbdotscepcdfz.npy', dots)
    # tmp = []
    # for i in range(dots.shape[0])
    # with open('../plotformalCSV/cepcdarkphoton/sbdotscepcdfh.ltxtb','w') as file_object:
    #     file_object.writelines()
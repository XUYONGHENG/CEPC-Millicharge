import numpy as np
import pandas as pd
import cut as cut



# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_ilc(s,bg,mass,cut=cut.cut_ilc_disposed_0,dataamount=5e6,splusb=False):

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

    a, b = np.load('/store/disposed/1211va/veveilcval.npy'), np.load('/store/disposed/1211va/vmvmilcvald.npy')
    b[:, -1] = 2 * b[:, -1]
    bg = np.vstack((a, b))

    # c,d = np.load('/store/disposed/vevecepc3d.npy'), np.load('/store/disposed/vmvmcepc3d.npy')
    # c, d = np.load('/store/disposed/vevecepc8d.npy'), np.load('/store/disposed/vmvmcepc8d.npy')
    # d[:,-1] = 2*d[:,-1]
    # bgraw = np.vstack((c,d))
    # print(np.sum(bgraw[:,-1]))
    # print(bgraw.shape)
    masses = np.linspace(1,201,51)
    # print(masses)
    dots = np.zeros(shape=(50, 2))

    for i in range(50):


        # Standard mq data. Generated w/ larger cut Formcalc.
        data = np.load('/store/disposed/milliq/ilc/mqilc132dot%dd.npy'%i)
        data[:,-1] = 1e-4*data[:,-1]
        dots[i,1] = signal_significance_ilc(s=data,
                            bg=bg,mass=masses[i],cut=cut.cut_ilc_disposed_0,dataamount=5e5,splusb=False)

        dots[i,0] = masses[i]
        print(dots[i])

    np.save('../plotCSV/sbdotsilc.npy',dots)

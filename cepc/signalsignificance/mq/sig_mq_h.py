import numpy as np
import cut as cut
from tools import signal_significance


# print(bg.shape)
# print(np.sum(bg[:,-1]))



if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    ### Standard bg w/o delphes.
    c,d = np.load('/store/disposed/finalpush/milliq/h/vebg.npy'),\
          np.load('/store/disposed/finalpush/milliq/h/vmbg.npy')
    d[:,-1] = 2*d[:,-1]
    bgraw = np.vstack((c,d))

    dots = np.zeros(shape=(201, 2))
    dots0 = np.zeros(shape=(2,2))

    # 0.1 - 1 add-ons. This is ugly, I know.

    dots0[0,0],dots0[1,0] = 0.1,0.5
    dots0[0, 1] = 1e2 * signal_significance(s=np.load('/store/disposed/milliq/cepch/mqh132m0.1d.npy'),
                                        bg=bgraw, mass=0.1, cut=cut.cut_cepc_advance_disposed_5, dataamount=5.6e6,
                                        splusb=False)[0]
    dots0[1, 1] = 1e2 * signal_significance(s=np.load('/store/disposed/milliq/cepch/mqh132m0.5d.npy'),
                                        bg=bgraw, mass=0.5, cut=cut.cut_cepc_advance_disposed_5, dataamount=5.6e6,
                                        splusb=False)[0]

    masses = 10**np.linspace(0,2,201)
    for i in range(201):


        # Standard mq data. Generated w/ larger cut Formcalc.
        # data = np.load('/store/disposed/milliq/mq132dot%dd.npy'%i)
        data = np.load('/store/disposed/finalpush/milliq/h/mqhx132%dd.npy'%(i))

        data[:,-1] = 1e-4*data[:,-1]
        print(np.sum(data[:,-1]))

        dots[i,1] = signal_significance(s=data,
                            bg=bgraw,mass=masses[i],
                            cut=cut.cut_cepc_advance_disposed_5,
                            dataamount=5.6e6,splusb=False)[0]
        dots[i,0] = masses[i]
        print(dots[i,1],'exclusion\n')

    dots = np.vstack((dots0,dots))
    print(dots.shape)
    print(dots)
    np.save('../plotCSV/mqh_formal_0.1-100.npy',dots)

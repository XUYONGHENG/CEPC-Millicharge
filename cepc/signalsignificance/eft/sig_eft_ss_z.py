import numpy as np
import cut as cut
from tools import signal_significance


# print(bg.shape)
# print(np.sum(bg[:,-1]))



if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    ### Standard bg w/o delphes.
    c,d = np.load('/store/disposed/finalpush/milliq/z/vebgz.npy'),\
          np.load('/store/disposed/finalpush/milliq/z/vmbgz.npy')
    d[:,-1] = 2*d[:,-1]
    bgraw = np.vstack((c,d))
    bgraw[:,-1] = (132.507/137)** 2 * bgraw[:,-1]

    print(np.sum(bgraw[:,-1]))

    dots = np.zeros(shape=(17, 2))

    # 0.1 - 1 add-ons. This is ugly, I know.

    masses = 10**np.linspace(0,2,21,endpoint=True)
    for i in range(17):


        # Standard mq data. Generated w/ larger cut Formcalc.
        # data = np.load('/store/disposed/milliq/mq132dot%dd.npy'%i)
        data = np.load('/store/disposed/finalpush/4fermion/ss/z/ss%dd.npy'%(i))

        print(np.sum(data[:,-1]))

        dots[i,1] = signal_significance(s=data,
                            bg=bgraw,mass=masses[i],
                            cut=cut.cut_cepcz_advance_disposed,
                            dataamount=16e6,splusb=False,is_epsilon=False)[0]
        dots[i,0] = masses[i]
        print(dots[i,1],'exclusion\n')

    print(dots.shape)
    print(dots)
    np.save('../plotCSV/eft_ss_z_formal_1-39.npy',dots)

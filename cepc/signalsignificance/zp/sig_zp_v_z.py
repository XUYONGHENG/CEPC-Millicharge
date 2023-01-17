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
    bgraw[:,-1] = (132.507/137)** 2 * bgraw[:,-1]

    dots = np.zeros(shape=(9, 2))

    # 0.1 - 1 add-ons. This is ugly, I know.

    masses = np.linspace(0,40,9,endpoint=True)
    print(masses)
    # input('halt')
    for i in range(9):


        # Standard mq data. Generated w/ larger cut Formcalc.
        # data = np.load('/store/disposed/milliq/mq132dot%dd.npy'%i)
        data = np.load('/store/disposed/finalpush/zp/z/v/mzz150v_mx%d_1-50d.npy'%(i+1))

        print(np.sum(data[:,-1]))

        dots[i,1] = signal_significance(s=data,
                            bg=bgraw,mass=masses[i],
                            cut=cut.cut_zp_iv_150_3z,
                            dataamount=16e6,splusb=False,is_epsilon=True)[0]
        dots[i,0] = masses[i]
        print(dots[i,1],'exclusion\n')

    print(dots.shape)
    print(dots)
    np.save('../../plotCSV/zp_v_z_formal_1-40.npy',dots)

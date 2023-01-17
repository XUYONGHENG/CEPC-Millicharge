import numpy as np
import cut as cut
from tools import signal_significance

# print(bg.shape)
# print(np.sum(bg[:,-1]))


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    ### Standard bg w/o delphes.
    b, a = np.load('/store/disposed/finalpush/milliq/z/vmbgz.npy'), np.load('/store/disposed/finalpush/milliq/z/vebgz.npy')
    b[:, -1] = 2 * b[:, -1]
    bgraw = np.vstack((b, a))


    dots = np.zeros(shape=(38, 2))
    dots0 = np.zeros(shape=(2, 2))

    # 0.1 - 1 add-ons. This is ugly, I know.

    dots0[0, 0], dots0[1, 0] = 0.1, 0.5
    dots0[0, 1] = 1e2 * signal_significance(s=np.load('/store/disposed/finalpush/milliq/z/mqz132m0.1d.npy'),
                                            bg=bgraw, mass=0.1, cut=cut.cut_cepcz_advance_disposed, dataamount=16e6,
                                            splusb=False)[0]
    dots0[1, 1] = 1e2 * signal_significance(s=np.load('/store/disposed/finalpush/milliq/z/mqz132m0.5d.npy'),
                                            bg=bgraw, mass=0.5, cut=cut.cut_cepcz_advance_disposed, dataamount=16e6,
                                            splusb=False)[0]

    masses = range(1,39)
    for i in range(38):
        # Standard mq data. Generated w/ larger cut Formcalc.
        # data = np.load('/store/disposed/milliq/mq132dot%dd.npy'%i)
        data = np.load('/store/disposed/finalpush/milliq/z/mqzx132%dd.npy' % (i+1))

        data[:, -1] = 1e-4 * data[:, -1]
        print(np.sum(data[:, -1]))

        dots[i, 1] = signal_significance(s=data,
                                         bg=bgraw, mass=masses[i],
                                         cut=cut.cut_cepcz_advance_disposed,
                                         dataamount=16e6, splusb=False)[0]
        dots[i, 0] = masses[i]
        print(dots[i, 1], 'exclusion\n')

    dots = np.vstack((dots0, dots))
    print(dots.shape)
    print(dots)
    np.save('../plotCSV/mqz_formal_0.1-38.npy', dots)

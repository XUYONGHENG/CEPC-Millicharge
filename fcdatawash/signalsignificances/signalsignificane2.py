import numpy as np
import cut as cut


# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_d3(s,bg,mass,cut=cut.cut_cepc_advance_disposed_2,dataamount=5e6,splusb=False):
    print(mass,'mass')
    ssection = 0
    # count = 0


    for i in range(s.shape[0]):
        if cut(s[i],mass):
            ssection += s[i,-1]
            # count += 1
    print(ssection,'s\n')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mass):
            bgsection += bg[i,-1]
    print(bgsection,'b\n')

    if not splusb:
        # print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01)
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount)))*0.01)


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    # a, b = np.load('/store/disposed/vevecepc2d.npy'), np.load('/store/disposed/vmvmcepc2d.npy')
    # b[:, -1] = 2 * b[:, -1]
    # bg = np.vstack((a, b))
    bgd = np.load('/store/disposed/test3_delpd.npy')
    # data1 = np.load('/store/eeeea/dot6xd.npy')
    bgd = np.column_stack((bgd, 8.1 / 1000000 * np.ones(shape=(bgd.shape[0]))))



    ### Standard bg w/o delphes.
    c,d = np.load('/store/disposed/vevecepc3d.npy'), np.load('/store/disposed/vmvmcepc3d.npy')
    # c, d = np.load('/store/disposed/vevecepc8d.npy'), np.load('/store/disposed/vmvmcepc8d.npy')
    d[:,-1] = 2*d[:,-1]
    bgraw = np.vstack((c,d))
    print(np.sum(bgraw[:,-1]))
    # print(bgraw.shape)
    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dots = np.zeros(shape=(21, 2))
    dots0 = np.zeros(shape=(2,2))
    dots0[0,0],dots0[1,0] = 0.1,0.5
    dots0[0, 1] = 1e2 * signal_significance_d3(s=np.load('/store/disposed/milliq/cepch/mqh132m0.1d.npy'),
                                        bg=bgraw, mass=0.1, cut=cut.cut_cepc_advance_disposed_2, dataamount=5.6e6,
                                        splusb=False)
    dots0[1, 1] = 1e2 * signal_significance_d3(s=np.load('/store/disposed/milliq/cepch/mqh132m0.5d.npy'),
                                        bg=bgraw, mass=0.5, cut=cut.cut_cepc_advance_disposed_2, dataamount=5.6e6,
                                        splusb=False)

    for i in range(0,21):


        # Standard mq data. Generated w/ larger cut Formcalc.
        data = np.load('/store/disposed/milliq/mq132dot%dd.npy'%i)
        data[:,-1] = 1e-4*data[:,-1]
        # print(data.shape)
        # print(np.sum(data[:,-1]))
        # print(np.sum(data[:,-1]))

        # data = np.load('/store/disposed/xxcepc1d.npy')
        # data = np.load('/store/disposed/mqm1del_delpd.npy')
        # data = np.load('/store/disposed/deldata%d_delpd.npy'%(i+1))
        # print(data.shape)
        # input('halt')
        # delpdcs = [4.004,4.003,3.884,3.811,3.741,3.677,3.6,3.539,
        #            3.474,3.395,3.342,3.263,3.197,3.123,3.048,2.967,2.877,2.764,2.586,2.292,1.632]
        # data = np.column_stack((data, 0.403*0.87 / 1000000 * np.ones(shape=(data.shape[0]))))
        # data = np.column_stack((data,delpdcs[i]*1e-11*np.ones(shape=(data.shape[0]))))
        # print(data.shape)
        # print(np.sum(data[:,-1]))
        # input('halt')
        dots[i,1] = signal_significance_d3(s=data,
                            bg=bgraw,mass=masses[i],cut=cut.cut_cepc_advance_disposed_2,dataamount=5.6e6,splusb=False)
        dots[i,0] = masses[i]
        print(dots[i,1],'exclusion\n')

    dots = np.vstack((dots0,dots))
    print(dots.shape)
    print(dots)
    np.save('../plotCSV/sbdots_newcut.npy',dots)

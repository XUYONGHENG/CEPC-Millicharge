import numpy as np
import cut as cut


# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_d3(s,bg,mass,cut=cut.cut_cepc_advance_disposed_2,dataamount=5e6,splusb=False):

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
    # print(np.sum(bgraw[:,-1]))
    # print(bgraw.shape)
    masses = 10**np.linspace(0,2,21)
    # print(masses)
    dots = np.zeros(shape=(21, 2))
    dots0 = np.zeros(shape=(2,2))
    dots0[0,0],dots0[1,0] = 0.1,0.5
    dots0[0, 1] = 1e2 * signal_significance_d3(s=np.load('/store/disposed/milliq/cepch/mqh132m0.1eta313d.npy'),
                                        bg=bgraw, mass=0.1, cut=cut.cut_cepc_advance_disposed_2_eta313, dataamount=5e6,
                                        splusb=False)
    dots0[1, 1] = 1e2 * signal_significance_d3(s=np.load('/store/disposed/milliq/cepch/mqh132m0.5eta313d.npy'),
                                        bg=bgraw, mass=0.5, cut=cut.cut_cepc_advance_disposed_2_eta313, dataamount=5e6,
                                        splusb=False)


    # for i in range(0,21):
    #
    #     data = np.load('/store/disposed/mq132dot%dd.npy'%i)
    #     data[:,-1] = 1e-4*data[:,-1]
    #
    #     dots[i,1] = signal_significance_d3(s=data,
    #                         bg=bgraw,mass=masses[i],cut=cut.cut_cepc_advance_disposed_2,dataamount=5e6,splusb=False)
    #     dots[i,0] = masses[i]
    #     print(dots[i,1])

    dots = np.vstack((dots0,dots))
    # print(dots.shape)
    np.save('../plotCSV/sbdotsdel2_eta313.npy',dots0)

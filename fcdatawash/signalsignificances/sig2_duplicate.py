import numpy as np
import cut as cut


# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_d4(s,bg,mass,cut=cut.cut_cepc_advance_disposed_2,dataamount=5e6,splusb=False):
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
    data = np.load('/store/disposed/milliq/mq132dot10d.npy')
    data[:, -1] = 1e-4 * data[:, -1]
    signal_significance_d4(s=data,bg=bgraw,mass=10,cut=cut.cut_cepc_basicadvacncd,dataamount=5e6,splusb=False)



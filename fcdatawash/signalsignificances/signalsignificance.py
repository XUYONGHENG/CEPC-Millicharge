import numpy as np
import pandas as pd
import cut as cut
import matplotlib.pyplot as plt


# bg1 = np.load('/store/tmp/veve1cepctmp.npy')
# bg2 = np.load('/store/tmp/vmvm1cepctmp.npy')
# bg1 = np.column_stack((bg1,np.array(pd.read_csv('/store/eevva/veve1cepcw.dat'))))
# bg2 = np.column_stack((bg1,2*np.array(pd.read_csv('/store/eevva/vmvm1cepcw.dat'))))


# input('halt')
# a = np.load('/store/tmp/dot1xtmp.npy')
# print(a.shape)
# b = np.array(pd.read_csv('/store/eevva/vmvm1cepcw.dat'))
# b = 3.3*1e-5/1000000 * np.ones(shape=(a.shape[0]))
# a = np.column_stack((a,b))
# print(a.shape)
# np.save('vebg.npy',bg1)
# np.save('vbg.npy',bg2)

# print(a[0,1]**2+a[0,2]**2+a[0,0]**2-a[0,3]**2)
# print(a[0])
def mass_check(p):
    if -p[0]**2+p[1]**1+p[2]**2+p[3]**2 - 10000 > 1e-5:
        print('bing!')

def massless_check(p):
    if -p[0]**2+p[1]**1+p[2]**2+p[3]**2 > 1e-5:
        print('bing!')


# for i in range(a.shape[0]-1):
#     mass_check(a[i,:4])
#     mass_check(a[i,4:])
#     mass_check(a[i,8:])
# flags = np.zeros(shape=(a.shape[0]))
# for i in range(flags.shape[0]):
#     if cut.cut_12_cepc_1_irredu(a[i]):
#         flags[i] = 1
# c = 0
# b = np.zeros(shape=(int(np.sum(flags)),13))
# for i in range(flags.shape[0]):
#     if flags[i]:
#         b[c] = a[i]
#         c += 1
#
# t = 0
# f = 0
# sum = 0
# for i in range(b.shape[0]):
#     # print(cut.cut_custom(a[i]))
#     if cut.cut_cepc_advance(b[i,:12],mass=100):
#         t += 1
#         sum += b[i,-1]
#     else:
#         f += 1

# print(sum)
def signal_significance_aftercut(s,bg,mass):
    ssection = 0
    for i in range(s.shape[0]):
        if cut.cut_cepc_advance(s[i,:12],mass):
            ssection += s[i,-1]

    print(ssection)
    bgsection = 0
    for b in bg:
        for i in range(b.shape[0]):
            if cut.cut_cepc_advance(b[i,:12],mass):
                bgsection += b[i,-1]
    # print(bgsection)
    return (np.sqrt(2/(ssection*5e6/np.sqrt(bgsection*5e6)))*0.01)
    # return ssection/bgsection


def signal_significance_d2(s,bg,mass,d=0,dataamount=5e6):
    ssection = 0
    count = 0
    if d == 2:
        for i in range(s.shape[0]):
            if cut.cut_cepc_advance_disposed_2(s[i],mass):
                ssection += s[i,-1]
                count += 1
        print(ssection)
        print('s')
        bgsection = 0
        for i in range(bg.shape[0]):
            if cut.cut_cepc_advance_disposed_2(bg[i],mass):
                bgsection += bg[i,-1]
        print(bgsection)
        print('b')
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01),count

    elif d == 1:
        for i in range(s.shape[0]):
            if cut.cut_cepc_advance_disposed(s[i]):
                ssection += s[i, -1]

        print(ssection)
        bgsection = 0
        for i in range(bg.shape[0]):
            if cut.cut_cepc_advance_disposed(bg[i]):
                bgsection += bg[i, -1]
        # print(bgsection)
        return (np.sqrt(2 / (ssection * dataamount / np.sqrt(bgsection * dataamount))) * 0.01)

    elif d == 3:
        for i in range(s.shape[0]):
            if cut.cut_cepc_advance_disposed_3(s[i], mass):
                ssection += s[i, -1]

        print(ssection)
        bgsection = 0
        for i in range(bg.shape[0]):
            if cut.cut_cepc_advance_disposed_3(bg[i], mass):
                bgsection += bg[i, -1]
        # print(bgsection)
        return (np.sqrt(2 / (ssection * dataamount / np.sqrt(bgsection * dataamount))) * 0.01)


def signal_significance_d2_4f(s,bg,mass,d=0,dataamount=5e6):
    ssection = 0
    if d == 2:
        for i in range(s.shape[0]):
            if cut.cut_cepc_advance_disposed_2_4f(s[i],mass):
                ssection += s[i,-1]

        print(ssection)
        print('\n')
        bgsection = 0
        for i in range(bg.shape[0]):
            if cut.cut_cepc_advance_disposed_2_4f(bg[i],mass):
                bgsection += bg[i,-1]
        print(bgsection)
        print('\n')
        return 1/np.sqrt(np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*2.5e-5)

    elif d == 1:
        for i in range(s.shape[0]):
            if cut.cut_cepc_advance_disposed(s[i]):
                ssection += s[i, -1]

        print(ssection)
        bgsection = 0
        for i in range(bg.shape[0]):
            if cut.cut_cepc_advance_disposed(bg[i]):
                bgsection += bg[i, -1]
        # print(bgsection)
        return 1/np.sqrt(np.sqrt(2 / (ssection * dataamount / np.sqrt(bgsection * dataamount))) * 2.5e-5)

    elif d == 3:
        for i in range(s.shape[0]):
            if cut.cut_cepc_advance_disposed_3(s[i], mass):
                ssection += s[i, -1]

        print(ssection)
        bgsection = 0
        for i in range(bg.shape[0]):
            if cut.cut_cepc_advance_disposed_3(bg[i], mass):
                bgsection += bg[i, -1]
        # print(bgsection)
        return 1/np.sqrt(np.sqrt(2 / (ssection * dataamount / np.sqrt(bgsection * dataamount))) * 2.5e-5)

if __name__ == '__main__':
    masses = 10 ** np.linspace(0, 2, 21, endpoint=True)

    bg2 = np.load('/store/eeeea/vmvm1cepcd.npy')
    bg2[:, -1] = 2 * bg2[:, -1]

    bg = np.row_stack((np.load('/store/eeeea/veve1cepcd.npy'), bg2))
    print(np.sum(bg[:, -1]))

    totalsections = np.array([3.557,3.532,3.52,3.496,3.469,3.448,3.412,3.375,3.327,3.276,3.224,3.150,3.096,
                              3.034,3.053,2.972,2.879,2.767,2.592,2.292,1.632])
    totalsections4 = np.array(
        [50.5, 50.39, 50.28, 50.39, 50.71, 50.72, 51.02, 51.25, 51.23, 51.54, 51.53, 51.58, 51.82, 52.09, 52.1, 52.37,
         52.41, 52.18, 50.93, 47.47, 35.94])

    print(totalsections.shape)
    dots = np.zeros(shape=(21,2))
    surviving_events = np.zeros_like(dots)
    dots[:,0] = 10**np.linspace(0,2,21,endpoint=True)
    surviving_events[:,0] = dots[:,0]
    for i in range(1,22):
        print('Mass: %f\n'%masses[i-1])
        # a = np.load('/store/eeeea/dot%dxd.npy'%i)
        a = np.load('/store/eeeea/xxee%dd.npy'%i)
        # print(a.shape)
        # b = np.array(pd.read_csv('/store/eevva/vmvm1cepcw.dat'))
        # b = totalsections[i-1] * 1e-5 / 1000000 * np.ones(shape=(a.shape[0]))
        b = totalsections4[i-1]/1000000*np.ones(shape=a.shape[0])
        a = np.column_stack((a, b))
        # print(a.shape)
        # np.save('vebg.npy', bg1)
        # np.save('vbg.npy', bg2)

        # dots[i-1,1],surviving_events[i-1,1] = signal_significance_d2(s=a,bg=bg,mass=masses[i-1],d=2)

        dots[i-1,1] = signal_significance_d2_4f(s=a,bg=bg,mass=masses[i-1],d=2,dataamount=2e7)

        print(dots[i-1,1])
    # ax,fig = plt.subplots()
    # ax.plot(dots[:,0],dots[:,1])
    # np.save('plotCSV/sbdots_adv.npy',dots)
    # np.save('plotCSV/surviving_adv',surviving_events)
    np.save('../plotCSV/4fsbdots7.npy',dots)
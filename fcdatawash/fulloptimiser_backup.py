import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cut as cut


class BackGround(object):
    def __init__(self,name,mode,data):
        self.name = name
        self.mode = mode
        self.data = data


class Signal(object):
    def __init__(self,name,mode,data):
        self.name = name
        self.mode = mode
        self.data = data

veh = np.load('/store/disposed/vevecepc3d.npy')
vmh = np.load('/store/disposed/vmvmcepc3d.npy')

vew = np.load('/store/disposed/milliq/cepcw/vmvmcepcwd.npy')
vmw = np.load('/store/disposed/milliq/cepcw/vevecepcwd.npy')

vez = np.load('/store/disposed/milliq/cepcz/vmvmcepczd.npy')
vmz = np.load('/store/disposed/milliq/cepcz/vevecepczd.npy')



def advcut_applier(signal,mode='h'):
    # Loading data & applying advcut.


    if mode == 'h':
        bge,bgm = veh,vmh
    elif mode == 'w':
        bge,bgm = vew,vmw
    elif mode == 'z':
        bge,bgm = vez,vmz


    # bgm [:,-1] = 2* bgm[:,-1]
    sig = signal

    # print(np.sum(bge[:, -1]), np.sum(bgm[:, -1]), np.sum(sig[:, -1]))

    # print(bge.shape, bgm.shape, sig.shape)
    ce, cm, cs = 0, 0, 0
    flage, flagm, flags = np.zeros(shape=(bge.shape[0])), np.zeros(shape=(bge.shape[0])), np.zeros(shape=(bge.shape[0]))

    for i in range(bge.shape[0]):
        if cut.cut_cepc_advance_disposed(bge[i],mode=mode):
            flage[i] = 1
            ce += 1
        if cut.cut_cepc_advance_disposed(bgm[i],mode=mode):
            flagm[i] = 1
            cm += 1

    for i in range(sig.shape[0]):
        if cut.cut_cepc_advance_disposed(sig[i], mode=mode):
            flags[i] = 1
            cs += 1

    print(ce, cm, cs)

    edisposed, mdisposed, sigdisposed = np.zeros(shape=(ce, 5)), np.zeros(shape=(cm, 5)), np.zeros(shape=(cs, 5))

    c = 0

    for i in range(bge.shape[0]):
        if flage[i]:
            edisposed[c] = bge[i]
            c += 1

    c = 0
    for i in range(bge.shape[0]):
        if flagm[i]:
            mdisposed[c] = bgm[i]
            c += 1

    c = 0
    for i in range(sig.shape[0]):
        if flags[i]:
            sigdisposed[c] = sig[i]
            c += 1

    mdisposed[:, -1] = 2 * mdisposed[:, -1]
    bgdisposed = np.vstack((edisposed, mdisposed))
    print(np.sum(bgdisposed[:,-1]))
    print(np.sum(sigdisposed[:,-1]))

    return np.column_stack((bgdisposed[:, 0], bgdisposed[:, 2], bgdisposed[:, -1])),np.column_stack((sigdisposed[:, 0], sigdisposed[:, 2], sigdisposed[:, -1]))

def binner(sig,bg,energy=240):

    # bg, sig = np.load('/store/disposed/bgadvcut2.npy'), np.load('/store/disposed/xxadvcut2.npy')
    energy = 0.5*energy

    # sig[:, -1] = 0.0001 * sig[:, -1]
    bg = bg
    # print(bg.shape,sig.shape,np.sum(bg[:,-1]),np.sum(sig[:,-1]))
    # print(np.max(sig[:,0]),np.min(sig[:,0]))
    print(np.min([np.max(sig[:,0]),energy]))
    # bin 30. The range is determined by the maximal value at each dot.
    binrange = np.array([[0.25*energy, np.min([np.max(sig[:,0]),energy])], [-1, 1]])

    bghist, bx, by = np.histogram2d(bg[:, 0], bg[:, 1], weights=bg[:, 2], bins=30, range=binrange)
    shist, sx, sy = np.histogram2d(sig[:, 0], sig[:, 1], weights=sig[:, 2], bins=30, range=binrange)
    print(bghist)
    print(shist)
    # plt.imshow(bghist)
    # plt.imshow(shist)
    # print(bx,by,sx,sy)
    ratio = np.zeros_like(bghist)
    for i in range(30):
        for j in range(30):
            try:
                ratio[i, j] = shist[i, j] / bghist[i, j]
            except ZeroDivisionError:
                if shist  != 0:
                    ratio[i, j] = 0
                else:
                    ratio[i, j] = 1e-8
    ratio = np.log10(np.nan_to_num(ratio))
    ratio[ratio == -np.inf] = 0
    # print(ratio)

    return ratio,shist,bghist


def epsiloncalc(s, b, l=5e6):
    return (np.sqrt(2 / (s * l / np.sqrt(b * l))) * 0.01)


def lambdacalc(s, b, l=5e6):
    print(s,b)
    return 1/np.sqrt(np.sqrt(2/(s*l/np.sqrt(b*l)))*2.5e-5)


def fulloptimiser(ratio,shist,bghist,luminosity = 5e6, ff=False):
    ratio, signal, bg = ratio,shist,bghist
    print('bing!')
    ratiodict = {}
    for i in range(30):
        for j in range(30):
            if ratio[i, j] != 0:
                # print(ratio[i,j])
                ratiodict[str(ratio[i, j])] = (i, j)

    # print(ratiodict)
    ratioflat = np.reshape(ratio, (900))
    flatorderd = (np.sort(ratioflat))
    # print(flatorderd)
    a = 0
    # print(flatorderd[800])
    # input()
    for i in range(flatorderd.shape[0]):
        # print(flatorderd)
        try:
            if flatorderd[i] != 0 and flatorderd[i + 1] == 0:
                a = i
                print('bing')
                print(a)
                break
        except IndexError:
            pass
            # print(flatorderd)
            # input('halt')

    # print(a)
    flatorderd = flatorderd[:a+1]
    flatorderd = flatorderd[::-1]

    epsilons = np.zeros(shape=(flatorderd.shape[0]))

    for i in range(flatorderd.shape[0]):
        stotal, bgtotal = 0, 0
        for k in range(i):
            cood = (ratiodict[str(flatorderd[k])])
            bins = (signal[cood[0], cood[1]])
            # print(type(bins))
            binbg = (bg[cood[0], cood[1]])
            stotal += bins
            # print(type(stotal))
            bgtotal += binbg
            # print(type(stotal))
        # print(stotal, bgtotal)
        if not ff:
            ep = epsiloncalc(s=stotal, b=bgtotal,l=luminosity)
        elif ff:
            ep = lambdacalc(s=stotal,b=bgtotal,l=luminosity)
        epsilons[i] = ep
        # print(type(ep))
    # print(epsilons)
    epsilons = epsilons[1:]
    # print(epsilons)
    # print(np.min(epsilons))
    # print(list(epsilons).index(np.min(epsilons)))
    # print(epsilons[23])
    # print(np.sort(epsilons)[1])
    # a = np.zeros_like(ratio)
    # for i in range(23):
    #     a[tuple(ratiodict[str(flatorderd[i])])] = 10
    if not ff:
        ep, nob = np.min(epsilons),list(epsilons).index(np.min(epsilons))
    elif ff:
        ep, nob = np.max(epsilons),list(epsilons).index(np.max(epsilons))
    coods = np.zeros(shape=(nob,2))
    for i in range(nob):
        coods[i] = np.array((ratiodict[str(flatorderd[i])]))
    # print(coods)
    return ep, nob, coods


def binplot(data):


    fig, ax = plt.subplots()

    im = ax.imshow(data, cmap='Greys')
    # ax.set_xticks(np.arange(30))
    # ax.set_xticklabels(str(np.linspace(-0.989,0.989,30)))
    ax.set_xticks(np.linspace(0, 30, 5))
    ax.set_xticklabels(np.linspace(-1, 1, 5))
    ax.set_yticks(np.linspace(0, 30, 5))
    ax.set_yticklabels(np.linspace(30, 120, 5))
    cbar = ax.figure.colorbar(im, ax=ax, cmap='Greys')
    cbar.ax.set_ylabel(r'-log($d\sigma_s/d\sigma_b)$', rotation=-90, va="bottom", fontsize=35)
    plt.suptitle('Signal/BG ratio', fontsize=32)
    ax.set_xlabel(r'cos$\theta_\gamma$', fontsize=32)
    ax.set_ylabel(r'$E_\gamma$', fontsize=32)

    plt.show()

if __name__ == '__main__':

    # print(np.sum(vmh[:,-1]))
    eps,ns = np.zeros(shape=(21,)),np.zeros(shape=(21,))
    for i in range(21):
        print(10**np.linspace(0,2,21)[i])
        signal = np.load('/store/disposed/mq132dot%dd.npy'%i)
        signal[:,-1] = 1e-4*signal[:,-1]
        # print(np.sum(signal[:,-1]))
        bgadv, sadv = advcut_applier(signal=signal, mode='h')
        ratio, shist, bghist = binner(sadv,bgadv,energy=240)
        # print(ratio)
        # fig, ax = plt.subplots()
        #
        # # ax.set_xticks(np.arange(30))
        # # ax.set_xticklabels(str(np.linspace(-0.989,0.989,30)))
        # ax.set_xticks(np.linspace(0, 30, 5))
        # ax.set_xticklabels(np.linspace(-1, 1, 5))
        # ax.set_yticks(np.linspace(0, 30, 5))
        # ax.set_yticklabels(np.linspace(30, 120, 5))
        # cbar = ax.figure.colorbar(im, ax=ax, cmap='Greys')
        # cbar.ax.set_ylabel(r'-log($d\sigma_s/d\sigma_b)$', rotation=-90, va="bottom", fontsize=35)
        # plt.suptitle('Signal/BG ratio', fontsize=32)
        # ax.set_xlabel(r'cos$\theta_\gamma$', fontsize=32)
        # ax.set_ylabel(r'$E_\gamma$', fontsize=32)
        #
        # plt.show()
        # np.save('/store/disposed/sbratiobin2.npy', ratio)
        # np.save('/store/disposed/sbin2.npy', shist)
        # np.save('/store/disposed/bgbin2.npy', bghist)
        # input('halt')
        ep,n,coodss = fulloptimiser(ratio, shist, bghist,luminosity=5e6,ff=False)
        print(ep)
        eps[i],ns[i] = ep,n
        if i == 0:
            np.save('plotCSV/selectedbins1.npy',coodss)
        elif i == 10:
            np.save('plotCSV/selectedbins10.npy',coodss)

    # np.save('plotCSV/sbdotsoptimised1.npy',eps)
    # print(ns)
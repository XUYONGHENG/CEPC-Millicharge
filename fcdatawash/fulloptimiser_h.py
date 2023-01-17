import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cut as cut


def advcut_applier(signal,bge,bgm):
    # Loading data & applying advcut.
    bge,bgm = bge,bgm
    # bgm [:,-1] = 2* bgm[:,-1]
    sig = np.load(signal)

    # print(np.sum(bge[:, -1]), np.sum(bgm[:, -1]), np.sum(sig[:, -1]))

    # print(bge.shape, bgm.shape, sig.shape)
    ce, cm, cs = 0, 0, 0
    flage, flagm, flags = np.zeros(shape=(bge.shape[0])), np.zeros(shape=(bge.shape[0])), np.zeros(shape=(bge.shape[0]))

    for i in range(bge.shape[0]):
        if cut.cut_cepc_advance_disposed(bge[i]):
            flage[i] = 1
            ce += 1
        if cut.cut_cepc_advance_disposed(bgm[i]):
            flagm[i] = 1
            cm += 1
        if cut.cut_cepc_advance_disposed(sig[i]):
            flags[i] = 1
            cs += 1

    # print(ce, cm, cs)

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
    for i in range(bge.shape[0]):
        if flags[i]:
            sigdisposed[c] = sig[i]
            c += 1

    mdisposed[:, -1] = 2 * mdisposed[:, -1]
    bgdisposed = np.vstack((edisposed, mdisposed))

    return np.column_stack((bgdisposed[:, 0], bgdisposed[:, 2], bgdisposed[:, -1])),np.column_stack((sigdisposed[:, 0], sigdisposed[:, 2], sigdisposed[:, -1]))

def binner(sig,bg):
    # bg, sig = np.load('/store/disposed/bgadvcut2.npy'), np.load('/store/disposed/xxadvcut2.npy')

    sig[:, -1] = 0.0001 * sig[:, -1]
    bg = bg
    # print(bg.shape,sig.shape,np.sum(bg[:,-1]),np.sum(sig[:,-1]))
    # print(np.max(sig[:,0]),np.min(sig[:,0]))
    print(np.min([np.max(sig[:,0]),120]))
    # bin 30. The range is determined by the maximal value at each dot.
    binrange = np.array([[30, np.min([np.max(sig[:,0]),120])], [-1, 1]])

    bghist, bx, by = np.histogram2d(bg[:, 0], bg[:, 1], weights=bg[:, 2], bins=30, range=binrange)
    shist, sx, sy = np.histogram2d(sig[:, 0], sig[:, 1], weights=sig[:, 2], bins=30, range=binrange)
    # print(bghist)
    # print(bx,by,sx,sy)
    ratio = np.zeros_like(bghist)
    for i in range(30):
        for j in range(30):
            try:
                ratio[i, j] = shist[i, j] / bghist[i, j]
            except ZeroDivisionError:
                ratio[i, j] = 0

    ratio = np.log10(np.nan_to_num(ratio))
    ratio[ratio == -np.inf] = 0

    return ratio,shist,bghist


def epsiloncalc(s, b):
    return (np.sqrt(2 / (s * 5e6 / np.sqrt(b * 5e6))) * 0.01)


def fulloptimiser(ratio,shist,bghist):
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
            print(flatorderd)
            input('halt')

    print(a)
    flatorderd = flatorderd[:a+1]
    flatorderd = flatorderd[::-1]

    # print(flatorderd)



    # print(epsiloncalc(1, 1))
    # input('halt')
    epsilons = np.zeros(shape=(flatorderd.shape[0]))
    # print(epsilons.shape)
    # input()
    # for i in range(flatorderd.shape[0]):
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
        ep = epsiloncalc(s=stotal, b=bgtotal)
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
    ep, nob = np.min(epsilons),list(epsilons).index(np.min(epsilons))
    coods = np.zeros(shape=(nob,2))
    for i in range(nob):
        coods[i] = np.array((ratiodict[str(flatorderd[i])]))
    print(coods)
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
    ve = np.load('/store/disposed/vevecepc3d.npy')
    vm = np.load('/store/disposed/vmvmcepc3d.npy')
    eps,ns = np.zeros(shape=(21,)),np.zeros(shape=(21,))
    for i in range(21):
        print(10**np.linspace(0,2,21)[i])
        bgadv, sadv = advcut_applier('/store/disposed/mq132dot%dd.npy'%i, ve, vm)
        ratio, shist, bghist = binner(sadv,bgadv)
        # fig, ax = plt.subplots()
        #
        # im = ax.imshow(ratio, cmap='Greys')
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
        ep,n,coodss = fulloptimiser(ratio, shist, bghist)
        print(ep)
        eps[i],ns[i] = ep,n
        if i == 0:
            np.save('plotCSV/selectedbins1.npy',coodss)
        elif i == 10:
            np.save('plotCSV/selectedbins10.npy',coodss)

    # np.save('plotCSV/sbdotsoptimised1.npy',eps)
    print(ns)
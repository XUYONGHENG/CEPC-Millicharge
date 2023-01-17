import numpy as np
import matplotlib.pyplot as plt
import cut as cut
import fulloptimiser_general as opt

# signal = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot16d.npy')
# print(signal.shape)
# input('halt')

if __name__ == '__main__':
    signalh01,signalz01,signalw01 = np.load('/store/disposed/milliq/cepch/mqh132m0.1d.npy'),np.load('/store/disposed/milliq/cepcz/mqz132m0.1d.npy'),np.load('/store/disposed/milliq/cepcw/mqw132m0.1d.npy')
    signalh05,signalz05,signalw05 = np.load('/store/disposed/milliq/cepch/mqh132m0.5d.npy'),np.load('/store/disposed/milliq/cepcz/mqz132m0.5d.npy'),np.load('/store/disposed/milliq/cepcw/mqw132m0.5d.npy')
    signal01 = signalw01[:]
    signal01[:,-1] = 1e-4*signal01[:,-1]
    signal01 = np.load('/store/disposed/cepcdfh_run5/cepcdfh_iv_mz150_mx101_run5d.npy')
    print(np.sum(signal01[:,-1]))
    bgadv, sadv = opt.advcut_applier(signal=signal01, mode='h')
    ratio, shist, bghist = opt.binner(sadv, bgadv, energy=240)
    ep, n, coodss = opt.fulloptimiser(ratio, shist, bghist, luminosity=5.6e6, ff=0)
    print(ep)
    input('halt')

    # eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))
    # for i in range(21):
    #     print(10**np.linspace(0,2,21)[i])
    #     signal = np.load('/store/disposed/mq132dot%dd.npy'%i)
    #     signal[:,-1] = 1e-4*signal[:,-1]
    #     # print(np.sum(signal[:,-1]))
    #     bgadv, sadv = opt.advcut_applier(signal=signal, mode='h')
    #     ratio, shist, bghist = opt.binner(sadv,bgadv,energy=240)
    #     ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=5.6e6,ff=False)
    #     print(ep)
    #     eps[i],ns[i] = ep,n
    # # input('halt')
    # np.save('plotformalCSV/optimised/sbdostcepch.npy',eps)
    # np.save('plotformalCSV/optimised/nbinscepch.npy',ns)


    eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))
    for i in range(16):
        print(10**np.linspace(0,2,21)[i])
        signal = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot%dd.npy'%i)
        signal[:,-1] = 1e-4*signal[:,-1]
        # print(np.sum(signal[:,-1]))
        bgadv, sadv = opt.advcut_applier(signal=signal, mode='z')
        ratio, shist, bghist = opt.binner(sadv,bgadv,energy=91.2)
        ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=1.6e7,ff=False)
        print(ep)
        eps[i],ns[i] = ep,n

    np.save('plotformalCSV/optimised/sbdostcepcz.npy',eps[:17])
    np.save('plotformalCSV/optimised/nbinscepcz.npy',ns[:17])


    eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))
    for i in range(19):
        print(10**np.linspace(0,2,21)[i])
        signal = np.load('/store/disposed/milliq/cepcw/mqw132dot%dd.npy'%i)
        signal[:,-1] = 1e-4*signal[:,-1]
        # print(np.sum(signal[:,-1]))
        bgadv, sadv = opt.advcut_applier(signal=signal, mode='w')
        ratio, shist, bghist = opt.binner(sadv,bgadv,energy=160)
        ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=2.6e6,ff=False)
        print(ep)
        eps[i],ns[i] = ep,n

    np.save('plotformalCSV/optimised/sbdostcepcw.npy', eps[:20])
    np.save('plotformalCSV/optimised/nbinscepcw.npy', ns[:20])




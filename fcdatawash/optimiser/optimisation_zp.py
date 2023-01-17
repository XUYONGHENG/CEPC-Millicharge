import numpy as np
import matplotlib.pyplot as plt
import cut as cut
import fulloptimiser_general as opt

# signal = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot16d.npy')
# print(signal.shape)
# input('halt')

if __name__ == '__main__':
    # eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))
    # for i in range(21):
    #     print(10**np.linspace(0,2,21)[i])
    #     signal = np.load('/store/disposed/darkphoton/cepcdfh%dd.npy'%i)
    #     # signal[:,-1] = 1e-4*signal[:,-1]
    #     # print(np.sum(signal[:,-1]))
    #     bgadv, sadv = opt.advcut_applier(signal=signal, mode='h')
    #     ratio, shist, bghist = opt.binner(sadv,bgadv,energy=240)
    #     ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=5.6e6,ff=False)
    #     print(ep)
    #     eps[i],ns[i] = ep,n
    #
    # np.save('../plotformalCSV/optimised/sbdostdfh.npy',eps)
    # np.save('../plotformalCSV/optimised/nbinsdfh.npy',ns)


    eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))
    for i in range(16):
        print(10**np.linspace(0,2,21)[i])
        signal = np.load('/store/disposed/darkphoton/cepcdfz%dd.npy'%i)
        if i == 0:
            signal[:,-1] = 0.1*signal[:,-1]
        # signal[:,-1] = 1e-4*signal[:,-1]
        # print(np.sum(signal[:,-1]))
        bgadv, sadv = opt.advcut_applier(signal=signal, mode='z')
        ratio, shist, bghist = opt.binner(sadv,bgadv,energy=91.2)
        ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=1.6e7,ff=False)
        print(ep)
        eps[i],ns[i] = ep,n

    np.save('../plotformalCSV/optimised/sbdostdfz.npy',eps[:16])
    np.save('../plotformalCSV/optimised/nbinsdfz.npy',ns[:16])


    # eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))
    # for i in range(19):
    #     print(10**np.linspace(0,2,21)[i])
    #     signal = np.load('/store/disposed/darkphoton/cepcdfw%dd.npy'%i)
    #     # signal[:,-1] = 1e-4*signal[:,-1]
    #     # print(np.sum(signal[:,-1]))
    #     bgadv, sadv = opt.advcut_applier(signal=signal, mode='w')
    #     ratio, shist, bghist = opt.binner(sadv,bgadv,energy=160)
    #     ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=2.6e6,ff=False)
    #     print(ep)
    #     eps[i],ns[i] = ep,n
    #
    # np.save('../plotformalCSV/optimised/sbdostdfw.npy', eps[:19])
    # np.save('../plotformalCSV/optimised/nbinscdfw.npy', ns[:19])




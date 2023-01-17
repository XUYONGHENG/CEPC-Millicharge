import numpy as np
import matplotlib.pyplot as plt
import cut as cut
import fulloptimiser_general as opt

# signal = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot16d.npy')
# print(signal.shape)
# input('halt')

if __name__ == '__main__':
    keys = ['ss','st','vv','av']
    for j in keys:
        eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))

        for i in range(21):
            print(10**np.linspace(0,2,21)[i])
            signal = np.load('/store/disposed/cepc4f%s/cepc4f%s%dd.npy'%(j,j,i))
            # signal[:,-1] = 1e-4*signal[:,-1]
            print(np.sum(signal[:,-1]))
            bgadv, sadv = opt.advcut_applier(signal=signal, mode='h')
            ratio, shist, bghist = opt.binner(sadv,bgadv,energy=240)
            # plt.imshow(ratio)
            # plt.show()
            # input('halt')
            # print(ratio)
            ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=5.6e6,ff=True)
            print(ep)
            eps[i],ns[i] = ep,n

        np.save('../plotformalCSV/optimised/sbdotseft%sh.npy'%j,eps)
        np.save('../plotformalCSV/optimised/nbinseft%sh.npy'%j,ns)


        eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))


        for i in range(16):
            print(10**np.linspace(0,2,21)[i])
            signal = np.load('/store/disposed/cepc4f%s/cepc4fz%s%dd.npy'%(j,j,i))
            # signal[:,-1] = 1e-4*signal[:,-1]
            # print(np.sum(signal[:,-1]))
            bgadv, sadv = opt.advcut_applier(signal=signal, mode='z')
            ratio, shist, bghist = opt.binner(sadv,bgadv,energy=91.2)
            ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=1.6e7,ff=True)
            print(ep)
            eps[i],ns[i] = ep,n

        np.save('../plotformalCSV/optimised/sbdosteft%sz.npy'%j,eps[:16])
        np.save('../plotformalCSV/optimised/nbinseft%sz.npy'%j,ns[:16])


        eps, ns = np.zeros(shape=(21,)), np.zeros(shape=(21,))



        for i in range(17):
            print(10**np.linspace(0,2,21)[i])
            signal = np.load('/store/disposed/cepc4f%s/cepc4fw%s%dd.npy'%(j,j,i))
            # signal[:,-1] = 1e-4*signal[:,-1]
            # print(np.sum(signal[:,-1]))
            bgadv, sadv = opt.advcut_applier(signal=signal, mode='w')
            ratio, shist, bghist = opt.binner(sadv,bgadv,energy=160)
            ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=2.6e6,ff=True)
            print(ep)
            eps[i],ns[i] = ep,n

        for i in range(17,19):
            print(10**np.linspace(0,2,21)[i])
            if j != 'ss':
                signal = np.load('/store/disposed/cepc4f%s/cepc4fw%s%d2d.npy'%(j,j,i))
            else:
                signal = np.load('/store/disposed/cepc4f%s/cepc4fw%s%dd.npy'%(j,j,i))

            # signal[:,-1] = 1e-4*signal[:,-1]
            # print(np.sum(signal[:,-1]))
            bgadv, sadv = opt.advcut_applier(signal=signal, mode='w')
            ratio, shist, bghist = opt.binner(sadv,bgadv,energy=160)
            ep,n,coodss = opt.fulloptimiser(ratio, shist, bghist,luminosity=2.6e6,ff=True)
            print(ep)
            eps[i],ns[i] = ep,n

        np.save('../plotformalCSV/optimised/sbdosteft%sw.npy'%j, eps[:19])
        np.save('../plotformalCSV/optimised/nbinseft%sw.npy'%j, ns[:19])




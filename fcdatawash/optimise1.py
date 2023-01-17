import numpy as np
import matplotlib.pyplot as plt


ratio,signal,bg = np.load('/store/disposed/sbratiobin2.npy'),np.load('/store/disposed/sbin2.npy'),np.load('/store/disposed/bgbin2.npy')

ratiodict = {}
for i in range(30):
    for j in range(30):
        if ratio[i,j] != 0:
            # print(ratio[i,j])
            ratiodict[str(ratio[i,j])] = (i,j)

# print(ratiodict)
ratioflat = np.reshape(ratio,(900))
flatorderd = (np.sort(ratioflat))
print(flatorderd)
# print(flatorderd)
# input()
# for i in range(flatorderd.shape[0]):
#     if flatorderd[i] == 0:
#         print(i)
# print(flatorderd[:818])
for i in range(flatorderd.shape[0]):
    if flatorderd[i] != 0 and flatorderd[i+1] == 0:
        a = i

flatorderd = flatorderd[:a+1]
flatorderd = flatorderd[::-1]

print(flatorderd)
# print(flatorderd)

def epsiloncalc(s,b):
    return (np.sqrt(2/(s*5e6/np.sqrt(b*5e6)))*0.01)

print(epsiloncalc(1,1))
# input('halt')
epsilons = np.zeros(shape=(flatorderd.shape[0]))
print(epsilons.shape)
# input()
# for i in range(flatorderd.shape[0]):
for i in range(flatorderd.shape[0]):
    stotal,bgtotal = 0,0
    for k in range(i):
        cood = (ratiodict[str(flatorderd[k])])
        bins = (signal[cood[0], cood[1]])
        # print(type(bins))
        binbg = (bg[cood[0], cood[1]])
        stotal += bins
        # print(type(stotal))
        bgtotal += binbg
        # print(type(stotal))
    # print(stotal,bgtotal)
    ep = epsiloncalc(s = stotal,b = bgtotal)
    epsilons[i] = ep
    # print(type(ep))
# print(epsilons)
epsilons = epsilons[1:]
print(epsilons)
print(np.min(epsilons))
# print(list(epsilons).index(np.min(epsilons)))
# print(epsilons[23])
# print(np.sort(epsilons)[1])
a = np.zeros_like(ratio)
for i in range(23):
    a[tuple(ratiodict[str(flatorderd[i])])] =10


# fig,ax = plt.subplots()
# im = ax.imshow(a,cmap='Greys')
# plt.suptitle('Suggested bins',fontsize =32)
# ax.set_xlabel(r'cos$\theta_\gamma$',fontsize=32)
# ax.set_ylabel(r'$E_\gamma$',fontsize=32)
# plt.show()

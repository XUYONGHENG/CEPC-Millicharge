import numpy as np
import matplotlib.pyplot as plt


a = np.load('../plotCSV/sb3dots313.npy')
b = np.load('../plotCSV/sb3dots8_5degree.npy')
c = np.load('../plotCSV/sb3dots10degree.npy')

print(c.shape)

d = 10**np.linspace(0,2,21)
fig, ax1 = plt.subplots()

l1, = ax1.plot(a[:,0],a[:,1],linewidth=2.4,linestyle='--')
l2, = ax1.plot(b[:,0],b[:,1],linewidth=2.4)
l3, = ax1.plot(c[:,0],c[:,1],linewidth=2.4,linestyle='-.')


ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.text(1,0.3,s=r'The effect of $\theta$ coverage on the exclusion line',fontsize=19)
ax1.text(2,0.15,s=r'$\sqrt{S}=240GeV, E_\gamma > 0.1 GeV$',fontsize=19)
ax1.text(2,0.085,s=r'$\int L dt = 5 ab^{-1}$',fontsize=19)


ax1.legend((l1,l2,l3),(r'$\theta=5\degree$',r'$\theta=8.5\degree$',r'$\theta=10\degree$'),fontsize=19)
ax1.set_xlabel(r'$m_\chi$ (GeV)',fontsize=18)
ax1.set_ylabel(r'$\epsilon$',fontsize=18)


ax1.set_xlim((0.5,120))
ax1.set_ylim((1e-2,1))


for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax1.xaxis.get_minor_ticks():
    tick.label.set_fontsize(12)
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax1.yaxis.get_minor_ticks():
    tick.label.set_fontsize(12)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# eps = np.array([0.01,0.0084,0.005,0.0042,0.00357])
# sbs = np.array([68,43.78,19,7,23.9])

# eps = 1e-2 * np.sqrt(0.5)**np.linspace(0,7,8)
# print(eps)
# sbs = np.array([194.62,97.5,48.75,24.38,12.18,6.08,3.07,1.50])
# input('halt')
x = 10**np.linspace(-3,-2,10)
# a = np.load('/store/disposed/visibledecay/mass91/resultnpmass91.npy')
a = np.load('/store/disposed/visibledecay/mass50/resultnpmass50.npy')
eps,sbs = a[:,0],a[:,1]

z1 = np.polyfit(eps,sbs,2)
p1 = np.poly1d(z1)
print(p1)
sbvals = p1(x)
# plt.plot(eps,sbs)
# plt.show()
fig,ax = plt.subplots()######################################################################

plot1 = plt.plot(eps,sbs,marker='*',linewidth=2)
plot2 = plt.plot(x,sbvals,linewidth=2)##########################################################
plt.text(0.006,10,'MC result',color='#1f77b4',fontsize=24)
plt.text(0.004,15,'2D fit',color='C1',fontsize=24)
plt.text(0.001,22,'100,000 events each',fontsize=24)
plt.text(0.0015,30,r'$\int Ldt=5ab^{-1}$,$m_{Z^\prime}=50$GeV',fontsize=24)



for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')###############################################################################
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')

ax.tick_params(which = 'major', length=14,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)

ax.set_xlabel(r'$g_f^V$',fontsize=16)
ax.set_ylabel(r'$S/\sqrt{B}$',fontsize=16)


plt.show()
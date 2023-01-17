import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Calculates the ratio of \sigma_s/\sigma_bg in each bin.

bg,sig = np.load('/store/disposed/bgadvcut2.npy'),np.load('/store/disposed/xxadvcut2_m1.npy')
sig10,sig100 = np.load('/store/disposed/xxadvcut2_m10.npy'),np.load('/store/disposed/xxadvcut2_m100.npy')
sig[:,-1] = 0.0001 * sig[:,-1]
sig10[:,-1] = 0.0001 * sig10[:,-1]
sig100[:,-1] = 0.0001 * sig100[:,-1]


# print(bg.shape,sig.shape,np.sum(bg[:,-1]),np.sum(sig[:,-1]))
# print(np.max(sig[:,0]),np.min(sig[:,0]))

binrange = np.array([[30,120],[-1,1]])
##########################################################################################################
bghist, bx, by = np.histogram2d(bg[:,0],bg[:,1],weights=bg[:,2],bins=30,range=binrange)
s1hist, sx, sy = np.histogram2d(sig[:,0],sig[:,1],weights=sig[:,2],bins=30,range=binrange)
s10hist, sx, sy = np.histogram2d(sig10[:,0],sig10[:,1],weights=sig10[:,2],bins=30,range=binrange)
s100hist, sx, sy = np.histogram2d(sig100[:,0],sig100[:,1],weights=sig100[:,2],bins=30,range=binrange)


# print(bghist)
# print(bx,by,sx,sy)
ratio1,ratio10,ratio100 = np.zeros_like(bghist),np.zeros_like(bghist),np.zeros_like(bghist)
for i in range(30):
    for j in range(30):
        try:
            ratio1[i,j] = s1hist[i,j]/bghist[i,j]
        except ZeroDivisionError:
            ratio1[i,j] = 0
for i in range(30):
    for j in range(30):
        try:
            ratio10[i,j] = s10hist[i,j]/bghist[i,j]
        except ZeroDivisionError:
            ratio10[i,j] = 0
for i in range(30):
    for j in range(30):
        try:
            ratio100[i,j] = s100hist[i,j]/bghist[i,j]
        except ZeroDivisionError:
            ratio100[i,j] = 0

# tmp1 = ratio1[0,0]
ratio1,ratio10,ratio100 = np.log10(np.nan_to_num(ratio1)),np.log10(np.nan_to_num(ratio10)),np.log10(np.nan_to_num(ratio100))
ratio1[ratio1 == -np.inf] = 0
ratio10[ratio10 == -np.inf] = 0
ratio100[ratio100 == -np.inf] = 0

# ratio = -1*ratio
# print(ratio)
# np.save('/store/disposed/sbratiobin2.npy',ratio)
# np.save('/store/disposed/sbin2.npy',shist)
# np.save('/store/disposed/bgbin2.npy',bghist)
# fig = plt.figure()
# ax1,ax2,ax3 = plt.subplot(1,3,1),plt.subplot(1,3,2),plt.subplot(1,3,3)
fig,ax1= plt.subplots()

def binhist(ax,ratio,flagc=False):
# ax.set_xticks(np.arange(30))
# ax.set_xticklabels(str(np.linspace(-0.989,0.989,30)))
    im = ax.imshow(ratio)
    ax.set_xticks(np.linspace(0,30,5))
    ax.set_xticklabels(np.linspace(-1,1,5))
    ax.set_yticks(np.linspace(0,30,5))
    ax.set_yticklabels(np.linspace(30,120,5))

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = ax.figure.colorbar(im, cax=cax)
    if flagc:
        cbar.ax.set_ylabel(r'-log($d\sigma_s/d\sigma_b)$', rotation=-90, va="bottom",fontsize=24)

    # ax.set_xlabel(r'cos$\theta_\gamma$',fontsize=12)
    # ax.set_ylabel(r'$E_\gamma$',fontsize=12)

binhist(ax1,ratio100,True)
# binhist(ax2,ratio10)
# binhist(ax3,ratio100,True)
# cbar.ax.set_ylabel(r'-log($d\sigma_s/d\sigma_b)$', rotation=-90, va="bottom",fontsize=12)

# ax1.set_title(r'$m_\chi$ = 1 GeV',fontsize=24)
ax1.set_xlabel(r'cos$\theta_\gamma$',fontsize=24)
ax1.set_ylabel(r'$E_\gamma$ (GeV)',fontsize=24)

for label in ax1.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax1.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax1.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax1.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')

# ax1.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
# ax1.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)



plt.show()
# np.save('/store/disposed/sbratiobin2.npy',ratio)
# np.save('/store/disposed/sbin2.npy',shist)
# np.save('/store/disposed/bgbin2.npy',bghist)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tools as tools
from scipy.interpolate import spline


xtc,xtcm = np.array(pd.read_csv("/home/xyh/PycharmProjects/cepc/plotCSV/xtlimitsd.csv",header=None)),\
np.array(pd.read_csv("/home/xyh/PycharmProjects/cepc/plotCSV/xtlimitsd_m.csv",header=None))
print(xtc,xtcm)
######
xtc = np.column_stack((xtcm,xtc))
xtc = np.vstack(([xtcm[0],0],xtc))
############
# a_mass = np.linspace(1,201,51)[:50]

fig,ax = plt.subplots(figsize=(9,6.75))


eftexclusion_h = np.load('../../plotCSV/eft_av_h_formal_1-100.npy')
eftexclusion_w = np.load('../../plotCSV/eft_av_w_formal_1-63.npy')
eftexclusion_z = np.load('../../plotCSV/eft_av_z_formal_1-39.npy')

eftexclusion_h = np.vstack((eftexclusion_h,[104,0]))
eftexclusion_w = np.vstack((eftexclusion_w[:-1],[70,0]))
eftexclusion_z = np.vstack((eftexclusion_z[:-1],[40,0]))

lh, = ax.plot(eftexclusion_h[:,0],eftexclusion_h[:,1],color='black',linewidth=3)
lw, = ax.plot(eftexclusion_w[:,0],eftexclusion_w[:,1],color='red',linewidth=3,linestyle='--')
lz, = ax.plot(eftexclusion_z[:,0],eftexclusion_z[:,1],color='blue',linewidth=3,linestyle=':')
lc, = ax.plot(xtc[:,0],xtc[:,1],color='green',linestyle='-.')

ax.set_xscale('log')
# ax.set_yscale('log')
font0 = {'family':'serif'}

for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24,fontfamily='serif')
ax.set_ylabel(r'$\Lambda_A$ (GeV)',fontsize=24,fontfamily='serif')

ax.text(1.2,1400,r'H-mode $\sqrt{s}$=240 GeV',fontsize=16,color='black',fontfamily='serif')
ax.text(1.2,800,r'WW-mode $\sqrt{s}$=160 GeV',fontsize=16,color='red',fontfamily='serif')
ax.text(1.2,1190,r'Z-mode $\sqrt{s}$=91.2 GeV',fontsize=16,color='blue',fontfamily='serif')
ax.text(8,620,r'XENON1T',fontsize=16,fontfamily='serif',color='green',rotation=65)

ax.text(1.2,550,'Axial Vector',fontsize=24,fontfamily='serif')

ax.set_xlim(1,120)
ax.set_ylim(200,1600)

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)

# plt.savefig('~/Desktop/test.png',format='png')
plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/eftrej_av_2.pdf',format='pdf')
plt.show()
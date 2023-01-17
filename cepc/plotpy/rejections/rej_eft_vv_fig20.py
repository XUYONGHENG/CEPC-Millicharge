import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tools as tools
from scipy.interpolate import spline




######
############
# a_mass = np.linspace(1,201,51)[:50]

fig,ax = plt.subplots(figsize=(9,6.75))



eftexclusion_h = np.load('../../plotCSV/eft_vv_h_formal_1-100.npy')
eftexclusion_h = np.vstack((eftexclusion_h,[104,0]))
eftexclusion_w = np.load('../../plotCSV/eft_vv_w_formal_1-63.npy')
eftexclusion_w = np.vstack((eftexclusion_w,[70,0]))
eftexclusion_z = np.load('../../plotCSV/eft_vv_z_formal_1-39.npy')
eftexclusion_z = np.vstack((eftexclusion_z,[40,0]))


print(eftexclusion_h)
lh, = ax.plot(eftexclusion_h[:,0],eftexclusion_h[:,1],color='black',linewidth=3)
lw, = ax.plot(eftexclusion_w[:,0],eftexclusion_w[:,1],color='red',linewidth=3,linestyle='dashed')
lz, = ax.plot(eftexclusion_z[:,0],eftexclusion_z[:,1],color='blue',linewidth=3,linestyle='dotted')


ax.set_xscale('log')
# ax.set_yscale('log')


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
ax.set_ylabel(r'$\Lambda_s$ (GeV)',fontsize=24,fontfamily='serif')


ax.text(2,1400,r'Higgs Factory $\sqrt{s}$=240 GeV',fontsize=20,color='black',fontfamily='serif')
ax.text(2,830,r'$W^+W^-$ $\sqrt{s}$=160 GeV',fontsize=20,color='red',fontfamily='serif')
ax.text(2,1050,r'$Z$-pole $\sqrt{s}$=91.2 GeV',fontsize=20,color='blue',fontfamily='serif')
ax.text(5,550,r'Vector',fontsize=24,fontfamily='serif')


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

plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/eftrej_vv_3.pdf',format='pdf')

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataiv0 = np.load('../plotformalCSV/couplings_gvxgvffixed2.npy')
dataiv = np.load('../plotformalCSV/couplings_gvxgvffixed.npy')
datav = np.load('../plotformalCSV/couplings_gvffixed.npy')
datav0 = np.load('../plotformalCSV/couplings_gvffixed2.npy')

dataiv = np.vstack((dataiv0,dataiv))
datav[:,0] = 10**np.linspace(-2,0,5)
datav = np.vstack((datav0,datav))
# print(dataiv0)
# input('halt')
fig, ax = plt.subplots(figsize=(12,9))
l1, = ax.plot(dataiv[:,0],dataiv[:,1],linewidth=3,linestyle='solid',c='blue')
l2, = ax.plot(datav[:,0],datav[:,1],linewidth=3,linestyle='dashed',c='red')

ax.text(1e-1,1.2e-2,r'$\mu^+\mu^-\gamma$',fontsize=25,color='red',rotation=20)
ax.text(1e-1,1.2e-3,r'$\bar{\chi}\chi\gamma$',fontsize=25,color='blue')

ax.text(1.5e-3,3e-4,r'Expected CEPC sensitivity on the $g^V_\chi-g^V_f$ plane',fontsize=25)
ax.text(1.1e-2,1.7e-4,r'$\sqrt{s}=240$ GeV',fontsize=25)


sub3 = 10**np.linspace(-3,-2,10)

# ax.fill_between(data,l1,l2)
limitplotv0 = np.vstack((datav[:2,],np.array([0.0093,0.0037])))
limitplotv1 = np.vstack((datav[3:,],np.array([0.0093,0.0037])))
limitplotiv0,limitplotiv1 = np.vstack((dataiv[:4,],np.array([0.0093,0.0037]))), np.vstack((np.array([0.0093,0.0037]),dataiv[5:,]))


ax.fill_between(limitplotv0[:,0],limitplotv0[:,1],y2=10,color='red',alpha=0.5)
ax.fill_between(limitplotiv1[:,0],limitplotiv1[:,1],y2=10,color='blue',alpha=0.5)
# ax.fill_between(dataiv[5:,0],dataiv[5:,1],y2=10,color='blue',alpha=0.5)
ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'$g_\chi^V$',fontsize=25)
ax.set_ylabel(r'$g_f^V$',fontsize=25)

ax.tick_params(which = 'major', length=8,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)

for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.set_xlim(1e-3,1)
ax.set_ylim(1e-4,1e-1)
# ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)

plt.savefig('../figformal/dfrej_couplings.pdf',format='pdf')
plt.show()
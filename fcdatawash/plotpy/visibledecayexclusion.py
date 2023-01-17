import matplotlib.pyplot as plt
import numpy as np

a = np.array([10,50,91.2,150,200])
b = np.array([5.9e-3,2.06e-3,3.6e-3,1e-3,6.5e-4])
fig,ax = plt.subplots()
ax.plot(a,b,linewidth=3)
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

ax.set_xlabel(r'$m_{Z^\prime}$',fontsize=16)
ax.set_ylabel(r'$g^V_f$',fontsize=16)

ax.text(50,5e-3,"Visible decay constraint",fontsize=19)

plt.show()
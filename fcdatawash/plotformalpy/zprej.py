import matplotlib.pyplot as plt
import numpy as np


data,data2 = np.load('/store/disposed/visibledecay/resultnp2.npy'),np.load('/store/disposed/visibledecay/resultnp2zpolev.npy')
a,b = data[:,0],data[:,1]
a2,b2 = data[:43,0],data2
print(b2)
print(data2[:42])


np.savetxt('../plotCSV/visibledots.csv',np.column_stack((a2,b2)),delimiter=', ')
np.savetxt('../plotCSV/visibledotsh.csv',data,delimiter=', ')
# input('halt')
fig,ax = plt.subplots()
ax.plot(a,b,linewidth=3,color='black')
ax.plot(a2,b2,linewidth=3,color='blue',linestyle=':')
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


ax.set_yscale('log')
ax.set_xscale('log')
ax.tick_params(which = 'major', length=14,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)

ax.set_xlabel(r'$m_{Z^\prime} (GeV)$',fontsize=16)
ax.set_ylabel(r'$g^V_f$',fontsize=16)

ax.text(10,1e-3,"Visible decay constraint",fontsize=19)
ax.text(10,8e-3,r'Z pole mode $\sqrt{S}$=91.2GeV',fontsize=16,color='blue')
ax.text(10,4e-3,r'Higgs Factory mode $\sqrt{S}$=240GeV',fontsize=16,color='black')

plt.show()
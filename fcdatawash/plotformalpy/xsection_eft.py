import numpy as np
import matplotlib.pyplot as plt


vaxsection = np.array(
    [50.44, 50.87, 50.42, 50.87, 50.65, 50.91, 50.91, 50.96, 51.02, 51.08, 51.14, 50.98, 50.4, 49.71, 48.35, 46.63,
     43.41, 38.48, 31.12, 20.48, 7.367])
sssection = np.array(
    [36.42, 36.73, 36.58, 36.8, 36.79, 36.89, 36.86, 37.11, 37.1, 37.22, 37.05, 36.88, 36.66, 36.13, 35.15, 33.8, 31.84,
     28.01, 22.57, 14.81, 5.331])
stsection = np.array(
    [14.62, 14.59, 14.61, 14.57, 14.69, 14.73, 14.8, 14.81, 14.79, 14.89, 14.87, 14.83, 14.84, 14.7, 14.64, 14.35,
     13.88, 13.1, 11.85, 9.805, 6.24])

vvsection = np.array(
    [58.12, 58.37, 58.55, 58.57, 58.64, 58.83, 59.21, 59.39, 59.4, 59.88, 59.62, 59.88, 60.18, 60.2, 60.54, 60.41,
     60.52, 60.24, 58.88, 54.67, 41.44])

mass = 10**np.linspace(0,2,21)


fig,ax = plt.subplots()


lns1, = ax.plot(mass, 1/1.07*vvsection,linewidth=3 ,linestyle='solid', label = 'temp')
lns2, = ax.plot(mass, sssection,linewidth=3 ,linestyle='-.', label = 'Rn')
lns3, = ax.plot(mass, 1/1.07*vaxsection,linewidth=3, linestyle='dashed', label = 'Swdown',color='red')
lns4, = ax.plot(mass, 1/1.07*stsection,linewidth=3 ,linestyle=':', label = 'temp')


ax.set_xscale('log')
ax.set_yscale('log')
# ax.set_ylim()

for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)


ax.legend((lns1,lns2,lns3,lns4),('Vector','Scalar(s)','Axial-vector','Scalar(t)'),loc='lower left',fontsize=24,framealpha=0)


ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24)

plt.show()
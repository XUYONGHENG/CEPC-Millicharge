import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('mathtext', default='regular')


mass = 10**np.linspace(0,2,21)
#
# mqxs = np.zeros((21,))

# for i in range(21):
#     mqxs[i] = np.sum(np.load('/store/disposed/mq132dot%dd.npy'%i)[:,-1])

# np.save('mqcepceta3xs.npy',mqxs)
mqxs = np.load('mqcepceta3xs.npy')
# print(mqxs[0])

zxsection = np.load('/store/disposed/milliq/cepcz/zxsection.npy')
wxsection = np.load('/store/disposed/milliq/cepcw/wxsection.npy')

print(zxsection)
print(wxsection)

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

fig = plt.figure()
ax,ax2 = plt.subplot(1,2,1),plt.subplot(1,2,2)

lns1, = ax.plot(mass, 1/1.07*vaxsection,linewidth=3, linestyle='dashed', label = 'Swdown',color='red')
lns2, = ax.plot(mass, sssection,linewidth=3 ,linestyle='dashed', label = 'Rn')
lns3, = ax.plot(mass, 1/1.07*stsection,linewidth=3 ,linestyle='dashed', label = 'temp')
lns4, = ax.plot(mass, 1/1.07*vvsection,linewidth=3 ,linestyle='dashed', label = 'temp')
# ax2 = ax.twinx()

lns2h, = ax2.plot(mass, mqxs*1e-4,linewidth=3, linestyle = 'solid',color='black')
lns2w, = ax2.plot(mass[:20],wxsection*1e-4,linewidth=3, linestyle = '-.',color='red')
lns2z, = ax2.plot(mass[:17],zxsection*1e-4,linewidth=3, linestyle = ':',color='blue')
# added these three lines
# lns = lns1+lns2+lns3
# labs = [l.get_label() for l in lns]
ax.legend((lns1,lns2,lns3,lns4,), ('Vector-Axial','Scalar s-channel','Scalar t-channel','Vector-Vector'), loc='lower left',fontsize=17)
ax2.legend((lns2h,lns2w,lns2z), ('Higgs Factory','W+W-','Z-pole'), loc='lower left',fontsize=17)

ax.set_xscale('log')
ax.set_yscale('log')
ax2.set_xscale('log')
ax2.set_yscale('log')

# ax.grid()
ax.set_xlabel(r"$m_\chi$ (GeV)",fontsize=24)
ax.set_ylabel(r"$\sigma$ (pb)",fontsize=24)
ax2.set_ylabel(r"$\sigma$ (pb)",fontsize=24)
ax2.set_ylim(1e-5, 1e-3)
ax.set_ylim(0,80)


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
for label in ax2.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')


plt.show()
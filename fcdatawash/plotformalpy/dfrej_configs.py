import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.load('../plotformalCSV/cepcdarkphoton/sbdotscepcdfh.npy')
b = np.load('../plotformalCSV/cepcdarkphoton/sbdotscepcdfw.npy')
c = np.load('../plotformalCSV/cepcdarkphoton/sbdotscepcdfz.npy')
d = np.load('../plotformalCSV/cepcdarkphoton/sbdotscepcdfh_add.npy')

ad = {}
for i in range(21):
    ad[str(a[i,0])] = a[i,1]
    ad[str(d[i,0])] = d[i,1]



tmp1 = list(ad.keys())
for i in range(len(tmp1)):
    tmp1[i] = float(tmp1[i])

tmp1 = np.sort(tmp1)
add = np.zeros(shape=(41,2))
for i in range(41):
    add[i,0],add[i,1] = tmp1[i],ad[str(tmp1[i])]
print(add)
# print(list(ad.keys()))
# ad = np.array(sorted(float(ad.keys())))
# input('halt')
mass = 10**np.linspace(0,2,21)
# a = np.load('../plotformalCSV/optimised/sbdostdfh.npy')
# b = np.load('../plotformalCSV/optimised/sbdostdfw.npy')
# c = np.load('../plotformalCSV/optimised/sbdostdfz.npy')
# c = np.load('../plotformalCSV/cepcdarkphoton/sbdotscepcdfz.npy')

print(c)
print(a)

print(a.shape)
print(b.shape)
print(b)
print(c.shape)

# d = np.vstack((a,b[-5:]))
# print(d.shape)

mass = 10**np.linspace(0,2,21)

fig, ax = plt.subplots(figsize=(12,9))

l1, = ax.plot(add[:,0],add[:,1],linewidth=3,linestyle='-.',c='black')
l2, = ax.plot(b[:,0],b[:,1],linewidth=3,linestyle='dashed',c='red')
l3, = ax.plot(c[:,0],c[:,1],linewidth=3,linestyle=':',c='blue')

# l4, = ax.plot(d[:,0],d[:,1],linewidth=5,linestyle='dashed',c='black',alpha=0.5)

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax.set_ylabel(r'$g_f^V$',fontsize=25)

visibleexclusion = np.array([[75,1.1e-3],[1000,1.1e-3]])

ax.fill_between(visibleexclusion[:,0],visibleexclusion[:,1],y2=10,color='brown',alpha=0.6)
ax.text(75,0.02,'Visible Exclusion',fontsize=24,rotation=-90,color='brown')

datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
datac[:,0] = 1e-9*datac[:,0]

datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
for i in range(2,8):
    datac[i,0] = 1
for i in range(12,17):
    datac[i,0] = 45
datac[12,1] = 2.434105e-1
datac[-2] = [100,0.70396]
datac[-1,0] = 100

# l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

# ax.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.3)
# ax.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.3)
# ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

ax.text(2,3.5e-4,s=r"CEPC constraints on $g_f^V$",fontsize=24)
ax.text(2,2e-4,s=r"$m_{Z'}=150$ GeV,$g_\chi^A=g_f^A=0,g_\chi^V=1$",fontsize=24)
# ax.text(1,0.,s=r'$\sqrt{S}=91.2GeV$,CEPC detector cuts & Advanced cuts',fontsize=36)
ax.set_xlim((1,100))
ax.set_ylim((1e-4,5e-2))
ax.tick_params(which = 'major', length=8,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)


# ax.legend((l1,l2,l3),(r'Higgs Factory',r'W+W-',r'Z pole'),fontsize=20,loc='upper left')
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


ax.text(1.6,0.0012,r'Higgs Factory $\sqrt{s}=240$ GeV $\int\cal{L}dt$=5 ab$^{-1}$',Fontsize=24,color='black')
ax.text(2,0.007,r'W+W- $\sqrt{s}=160$ GeV $\int\cal{L}dt$=2 ab$^{-1}$',Fontsize=24,color='red')
ax.text(1.5,0.02,r'Z-pole $\sqrt{s}=91.2$ GeV $\int\cal{L}dt$=16 ab$^{-1}$',Fontsize=24,color='blue')


ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)


plt.savefig('../figformal/dfrej_2.pdf',format='pdf')
plt.show()
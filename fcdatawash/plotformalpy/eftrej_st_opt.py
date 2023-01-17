import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mass = 10**np.linspace(0,2,21)

az = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fav.npy')
bz = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fss.npy')
cz = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fst.npy')
dz = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fvv.npy')



ssh = np.load('../plotformalCSV/optimised/sbdotseftssh.npy')
ssw = np.load('../plotformalCSV/optimised/sbdosteftssw.npy')
# ssz = np.load('../plotformalCSV/optimised/sbdosteftssz.npy')
ssz = bz[:,-1]


sth = np.load('../plotformalCSV/optimised/sbdotseftsth.npy')
stw = np.load('../plotformalCSV/optimised/sbdosteftstw.npy')#####################################
# stz = np.load('../plotformalCSV/optimised/sbdosteftstz.npy')
stz = cz[:,-1]


vvh = np.load('../plotformalCSV/optimised/sbdotseftvvh.npy')
vvw = np.load('../plotformalCSV/optimised/sbdosteftvvw.npy')
# vvz = np.load('../plotformalCSV/optimised/sbdosteftvvz.npy')
vvz = dz[:,-1]


avh = np.load('../plotformalCSV/optimised/sbdotseftavh.npy')
avw = np.load('../plotformalCSV/optimised/sbdosteftavw.npy')
# avz = np.load('../plotformalCSV/optimised/sbdosteftavz.npy')
avz = az[:,1]



# input('halt')
fig,ax = plt.subplots(figsize=(9,6.75))

# l1h, = ax.plot(mass[:ssh.shape[0]],ssh,linewidth=3,linestyle='solid',color='black')
# l1w, = ax.plot(mass[:ssw.shape[0]],ssw,linewidth=3,linestyle='dashed',color='red')
# l1z, = ax.plot(mass[:ssz.shape[0]],ssz,linewidth=3,linestyle=':',color='blue')
#
l1h, = ax.plot(mass[:sth.shape[0]],sth,linewidth=3,linestyle='solid',color='black')
l1w, = ax.plot(mass[:stw.shape[0]],stw,linewidth=3,linestyle='dashed',color='red')
l1z, = ax.plot(mass[:stz.shape[0]],stz,linewidth=3,linestyle=':',color='blue')

#
# l1h, = ax.plot(mass[:vvh.shape[0]],vvh,linewidth=3,linestyle='solid',color='black')
# l1w, = ax.plot(mass[:vvw.shape[0]],vvw,linewidth=3,linestyle='dashed',color='red')
# l1z, = ax.plot(mass[:vvz.shape[0]],vvz,linewidth=3,linestyle=':',color='blue')
#
#
# l1h, = ax.plot(mass[:avh.shape[0]],avh,linewidth=3,linestyle='solid',color='black')
# l1w, = ax.plot(mass[:avw.shape[0]],avw,linewidth=3,linestyle='dashed',color='red')
# l1z, = ax.plot(mass[:avz.shape[0]],avz,linewidth=3,linestyle=':',color='blue')


ax.set_xscale('log')
ax.set_ylim(600,1200)
ax.set_xlim(1,100)
# ax.set_yscale('log')


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

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\Lambda$ (GeV)',fontsize=24)

ax.text(2,1050,r'Higgs Factory $\sqrt{s}$=240Gev',fontsize=20,color='black')
ax.text(2,650,r'$W^+W^-$ $\sqrt{s}$=160Gev',fontsize=20,color='red')
ax.text(2,900,r'$Z$-pole $\sqrt{s}$=91.2Gev',fontsize=20,color='blue')
ax.text(5,740,'Scalar(t)',fontsize=24)


plt.savefig('../figformal/eftrej_st_opt.pdf')

plt.show()
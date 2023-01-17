import numpy as np
import cut as cut
import pandas as pd
import matplotlib.pyplot as plt


a = np.load('../plotCSV/sbdots_adv.npy')
aa = np.load('../plotCSV/sbdots_full8.npy')
b = np.load('../plotCSV/surviving_adv.npy')
bb = np.load('../plotCSV/surviving_full8.npy')

c = np.column_stack((a,aa[:,1]))

cc = np.column_stack((b,bb[:,1]))

ax1,ax2 = plt.subplot(2,1,1),plt.subplot(2,1,2)

l1, = ax1.plot(a[:,0],a[:,1])
l2, = ax1.plot(a[:,0],aa[:,1])
ax1.set_xlabel(r'$m_\chi (GeV)$',fontsize=25)
ax1.set_ylabel(r'$\epsilon$',fontsize=25)
ax1.set_yscale('log')
ax1.set_xscale('log')

ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.plot(b[:,0],b[:,1])
ax2.plot(b[:,0],bb[:,1])
ax2.set_xlabel(r'$m_\chi (GeV)$',fontsize=25)
ax2.set_ylabel(r'Surviving events',fontsize=25)
ax1.legend((l1,l2),('Advanced cut only','full cut set'),loc='8')
ax2.legend((l1,l2),('Advanced cut only','full cut set'),loc='upper right')



plt.show()
# print(c)
# print(cc)
# np.savetxt('plotCSV/adv.csv',c,delimiter=', ')
# np.savetxt('plotCSV/full.csv',cc,delimiter=', ')
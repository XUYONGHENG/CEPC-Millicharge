import numpy as np


mass = 10**np.linspace(0,2,21)
# for i in range(21):
#     print(i,mass[i])


a, b = np.load('/store/disposed/milliq/cepcz/vmvmcepczd.npy'), np.load('/store/disposed/milliq/cepcz/vevecepczd.npy')
# print(np.sum(a[:, -1]))
b[:, -1] = 2 * b[:, -1]
bg = np.vstack((a, b))
print(np.sum(bg[:, -1]))


c = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot0d.npy')
print(np.sum(c[:,-1]))

print(np.column_stack((bg[:50,0],bg[:50,0])).shape)

input('halt')
np.savetxt('plotCSV/cepczbg.csv',np.column_stack((bg[:,0],bg[:,2])),delimiter=', ')
np.savetxt('plotCSV/cepczsig.csv',np.column_stack((c[:,0],c[:,2])),delimiter=', ')


np.savetxt('plotCSV/cepczbgw.csv',bg[:,-1],delimiter=', ')
np.savetxt('plotCSV/cepczsigw.csv',c[:,-1],delimiter=', ')
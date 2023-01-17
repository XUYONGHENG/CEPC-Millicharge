import pandas as pd
import numpy as np
import cut as cut

# New data: More optimistic than previous one
# bge,bgm,sig = np.load('/store/disposed/vevecepc8d.npy'),np.load('/store/disposed/vmvmcepc8d.npy'),np.load('/store/disposed/xxcepc1d.npy')

# Good ol' data. ~0.03 at mx = 1 GeV
bge,bgm,sig = np.load('/store/disposed/vevecepc3d.npy'),np.load('/store/disposed/vmvmcepc3d.npy'),np.load('/store/disposed/mq132dot20d.npy')

bgm[:,-1] = 2 * bgm[:,-1]
print(np.sum(bge[:,-1]),np.sum(bgm[:,-1]),np.sum(sig[:,-1]))

print(bge.shape,bgm.shape,sig.shape)
ce,cm,cs = 0,0,0
flage,flagm,flags = np.zeros(shape=(bge.shape[0])),np.zeros(shape=(bge.shape[0])),np.zeros(shape=(bge.shape[0]))


for i in range(bge.shape[0]):
    if cut.cut_cepc_advance_disposed(bge[i]):
        flage[i] = 1
        ce += 1
    if cut.cut_cepc_advance_disposed(bgm[i]):
        flagm[i] = 1
        cm += 1
    if cut.cut_cepc_advance_disposed(sig[i]):
        flags[i] = 1
        cs += 1


print(ce,cm,cs)

edisposed, mdisposed, sigdisposed = np.zeros(shape=(ce,5)),np.zeros(shape=(cm,5)),np.zeros(shape=(cs,5))

c = 0

for i in range(bge.shape[0]):
    if flage[i]:
        edisposed[c] = bge[i]
        c += 1

c = 0
for i in range(bge.shape[0]):
    if flagm[i]:
        mdisposed[c] = bgm[i]
        c += 1

c = 0
for i in range(bge.shape[0]):
    if flags[i]:
        sigdisposed[c] = sig[i]
        c += 1


mdisposed[:,-1] = 2*mdisposed[:,-1]
bgdisposed = np.vstack((edisposed,mdisposed))
# print(bgdisposed.shape)
# print(np.sum(edisposed[:,-1]),np.sum(mdisposed[:,-1]),np.sum(sigdisposed[:,-1]))
# np.savetxt('plotCSV/bgadvcut2.csv',np.column_stack((bgdisposed[:,0],bgdisposed[:,2])),delimiter=', ')
# np.save('/store/disposed/bgadvcut2.npy',np.column_stack((bgdisposed[:,0],bgdisposed[:,2],bgdisposed[:,-1])))
# np.savetxt('plotCSV/bgadvcut2w.csv',(bgdisposed[:,-1]),delimiter=', ')
# np.savetxt('plotCSV/veadvcut.csv',np.column_stack((edisposed[:,0],edisposed[:,2])),delimiter=', ')
# np.savetxt('plotCSV/vmadvcut.csv',np.column_stack((mdisposed[:,0],mdisposed[:,2])),delimiter=', ')
# np.savetxt('plotCSV/xxadvcut.csv',np.column_stack((sigdisposed[:,0],sigdisposed[:,2])),delimiter=', ')
np.save('/store/disposed/xxadvcut2_m100.npy',np.column_stack((sigdisposed[:,0],sigdisposed[:,2],sigdisposed[:,-1])))

# np.save()


# np.savetxt('plotCSV/veadvcutw.csv',edisposed[:,-1],delimiter=', ')
# np.savetxt('plotCSV/vmadvcutw.csv',mdisposed[:,-1],delimiter=', ')
# np.savetxt('plotCSV/xxadvcutw.csv',sigdisposed[:,-1],delimiter=', ')
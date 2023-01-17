import numpy as np
import cut as cut
import tools as tools

# data0 = np.load('/store/disposed/1307validation.npy')
# print(np.max(data0[:,1]))
data = np.load('/store/disposed/eenoecut2d.npy')
# print(np.max(data[:,1]))
# print(data[:10,2])
# print(data.shape)
print(np.sum(data[:,-1]))
# for i in range(data.shape[0]):
#     survivingsigma = 0
#     if cut.cut_4_1307_cut2(data[i]):
data2,sigma2 = tools.general_4_cut_applier(data=data,cut=cut.cut_4_1307_cut2)
data3,sigma3 = tools.general_4_cut_applier(data=data2,cut=cut.cut_4_1307_cut3_1)
data4,sigma4 = tools.general_4_cut_applier(data=data3,cut=cut.cut_4_1307_cut4)
print(sigma2,sigma3,sigma4)
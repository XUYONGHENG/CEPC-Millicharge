import numpy as np
import re as re
import pandas as pd
import matplotlib.pyplot as plt
from cut import cut,cut2,cut_besiii


#
# disposed = []
#
# with open("/store/eeeea/qed4.dat") as file_object:
#     raw = file_object.readlines()
#     for i in raw:
#         j = re.sub(r'\s+',', ',i.lstrip())
#         disposed.append(j[:-2]+"\n")
#
# print(disposed[-20:])
# input("hello")
# 利用re模块和简单的正则表达式实现去不特定空格的效果
# 显式地加入换行符以对抗弱智的writeline函数.
with open("qed4.csv",'w') as f:
    f.writelines(disposed)

a = np.array(pd.read_csv("qed4.csv"))
np.save("data/qed4GeV",a)
#
# input("3")

loaded = np.load("data/qed4GeV.npy")
print(loaded.shape)
# np.save("data/no_cut_250GeV_100000.npy",loaded)
# flag_939 = np.zeros(shape=(loaded.shape[0],))
# flag_984 = np.zeros_like(flag_939)
# flag_besiii = np.zeros(shape=(loaded.shape[0],))
# print(loaded[-1])
# for i in range(loaded.shape[0]):
#     if cut(loaded[i]):
#         flag_939[i] = 1
#     if cut2(loaded[i]):
#         flag_984[i] = 1
    # if cut_besiii(loaded[i]):
    #     flag_besiii[i] = 1


# print(np.sum(flag_939),np.sum(flag_984))
# input()
# cutmomenta939,cutmomenta984 = np.zeros(shape=(int(np.sum(flag_939)),12)),np.zeros(shape=(int(np.sum(flag_984)),12))
# cutmomentabesii_4GeV = np.zeros(shape=(int(np.sum(flag_besiii)),12))
# a,b = 0,0
# c = 0

def raw_to_momentum(p):
    tmp = np.zeros(shape=(12,))
    tmp[0],tmp[4],tmp[8]=loaded[i][0],loaded[i][5],loaded[i][10]
    tmp[1],tmp[2],tmp[3]=loaded[i][4]*loaded[i][1],loaded[i][4]*loaded[i][2],loaded[i][4]*loaded[i][3]
    tmp[5], tmp[6], tmp[7] = loaded[i][9] * loaded[i][6], loaded[i][9] * loaded[i][7], loaded[i][9] * loaded[i][8]
    tmp[9], tmp[10], tmp[11] = loaded[i][14] * loaded[i][11], loaded[i][14] * loaded[i][12], loaded[i][14] * loaded[i][13]
    return tmp

pqed4 = np.zeros(shape=(loaded.shape[0],12))
for i in range(loaded.shape[0]):
    # if flag_939[i]:
    #     cutmomenta939[a]=raw_to_momentum(loaded[i])
    #     a+=1
    # if flag_984[i]:
    #     cutmomenta984[b]=raw_to_momentum(loaded[i])
    #     b+=1
    # if flag_besiii[i]:
    #     cutmomentabesii_4GeV[c] = raw_to_momentum(loaded[i])
    #     c+=1
    pqed4[i] = raw_to_momentum(loaded[i])

# np.save("cutp939_4GeV.npy",cutmomenta939)
# np.save("cutp984_4GeV.npy",cutmomenta984)
np.save("data/pqed4nocut",pqed4)
# np.save("0.984cut_flag_4GeV",flag_984)
# np.save("0.939cut_flag_4GeV",flag_939)
# print(loaded.shape[0])
# flag_984 = np.load("0.984cut_flag_4GeV.npy")
# disposed_1 = np.zeros(shape=(loaded.shape[0],12))
# n = 0
# for i in range(loaded.shape[0]):
#     tmp = np.zeros(shape=(12,))
#     tmp[0],tmp[4],tmp[8]=loaded[i][0],loaded[i][5],loaded[i][10]
#     tmp[1],tmp[2],tmp[3]=loaded[i][4]*loaded[i][1],loaded[i][4]*loaded[i][2],loaded[i][4]*loaded[i][3]
#     tmp[5], tmp[6], tmp[7] = loaded[i][9] * loaded[i][6], loaded[i][9] * loaded[i][7], loaded[i][9] * loaded[i][8]
#     tmp[9], tmp[10], tmp[11] = loaded[i][14] * loaded[i][11], loaded[i][14] * loaded[i][12], loaded[i][14] * loaded[i][13]
#     disposed_1[n] = tmp
#     n+=1
    # if n%100000 == 0:
    #     n = 0
    #     break

# np.save("momenta_4GeV_nocut",disposed_1)
# 牺牲内存效率换来效率的大大提升.
# 总的来说,不要重复调用vstack函数. 估计最后nparray的形状,初始化一个同形状的纯零矩阵,再把值赋给它.
# np.save("disposed_nocut4GeV",disposed_1[:])
# a = np.load("momenta_4GeV_nocut.npy")
# print(a.shape)
# for i in range(a.shape[0]):
#     if np.abs(a[i][1]+a[i][5]+a[i][9]) > 1e-8:
#         print("bing!")
#     if np.abs(a[i][2]+a[i][6]+a[i][10]) > 1e-8:
#         print("bing!")
#     if np.abs(a[i][3]+a[i][7]+a[i][11]) > 1e-8:
#         print("bing!")
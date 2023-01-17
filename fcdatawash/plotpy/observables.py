import numpy as np

# # a = np.random.randint(0,1000000)
# data = np.load("momenta_4GeV_nocut.npy")
# # print(data[a,-4:])
# # print(data.shape)
# # print(data[-500:])
# # input('halt here')
# # print(data.shape)
# # print(data[:100])
# data939 = np.load("cutp939_4GeV.npy")
# data984 = np.load("cutp984_4GeV.npy")
data = np.load("data/pqed4nocut.npy")
print(data.shape)
# input("x")

def cos_theta_l1(p):
    return p[3]/p[0]

def cos_theta_l2(p):
    return p[7]/p[4]

def cos_theta_a(p):
    return p[11]/p[8]

def phi(p):
    return np.arctan(p[1]/p[2])

def eta(theta):
    return -np.log(np.tan(theta/2))

def lepton_invariant_mass(p):
    return (p[0]+p[4])**2-(p[1]+p[5])**2-(p[2]+p[6])**2-(p[3]-p[7])**2

def pt(p):
    return np.sqrt(p[1]**2+p[2]**2)

# print(cos_theta_a(data939[0]))
# data = [data939,data984]


# for j in range(2):
ob = np.zeros(shape=(data.shape[0], 16))
for i in range(ob.shape[0]):
    ob[i][0] = data[i][0]
    ob[i][1] = data[i][4]
    ob[i][2] = data[i][8]
    ob[i][3] = cos_theta_l1(data[i])
    ob[i][4] = cos_theta_l2(data[i])
    ob[i][5] = cos_theta_a(data[i])
    ob[i][6] = pt(data[i])
    ob[i][7] = pt(data[i,4:])
    ob[i][8] = pt(data[i,8:])
    ob[i][9] = eta(ob[i,3])
    ob[i][10] = eta(ob[i,4])
    ob[i][11] = eta(ob[i,5])
    ob[i][12] = lepton_invariant_mass(data[i])
    ob[i][13] = phi(data[i])
    ob[i][14] = phi(data[i,4:])
    ob[i][15] = phi(data[i,8:])
    # if not j:
    #     np.save("ob939_4GeV.npy",ob)
    # else:
    #     np.save("ob984_4GeV.npy",ob)
np.save("data/pqed4withob.npy",np.hstack((data,ob)))
# np.save("filtered939_4GeV.npy",np.hstack((data939,np.load("ob939_4GeV.npy"))))
# np.save("filtered984_4GeV.npy",np.hstack((data984,np.load("ob984_4GeV.npy"))))
# print(np.load("filtered939_4GeV.npy").shape)
# print(np.load("filtered984_4GeV.npy").shape)

# 0~2: Energies
# 3~5: CosTheta
# 6~8: pT
# 9~11: Rapidity
# 12: Lepton invariant Mass
# 13~15: Phi

# np.save("ob_1",ob)
# cos_theta = np.zeros((data.shape[0],))
# for i in range(data.shape[0]):
#     cos_theta[i] = pt(data[i,8:])
# print(cos_theta.shape[0])
# np.save("pt_a_1",cos_theta)
# print(cos_theta[:500000])
# plt.scatter(cos_theta[:250000],data[:250000,8],s=1)
# plt.xlabel(r'$Cos\theta_\gamma$')
# plt.ylabel(r'$E_\gamma$ (GeV)')
# plt.grid(True)
# plt.show()
# plt.hist(cos_theta[:1000],range=(-1,1),bins=200)
# plt.show()



# dot = np.zeros(shape=(data.shape[0],))
# print(dot.shape)
# for i in range(data.shape[0]):
#     dot[i] = cos_theta_l1(data[i])
# print(dot[:100])

# data_cutted = {}
# n = 0
# for i in range(data.shape[0]):
#     if np.abs(cos_theta_l1(data[i])) > 0.93:
#         if np.abs(cos_theta_l2(data[i]))>0.93:
#             if np.abs(cos_theta_a(data[i]))<0.93:
#                 if data[i][8] > 10:
#                     data_cutted[str(n)]=data[i]
#                     n+=1

# data_cutted = np.array(list(data_cutted.values()))
# print(data_cutted.shape)

# plt.hist(dot,range=(-1,1),bins=200)
# plt.xlabel("Lepton 1 angular distribution")
# plt.ylabel("count")
# plt.grid(True)
# plt.savefig("a distribution.png")
# plt.show()

# flag_939, flag_984, momenta = np.load("0.939cut_flag_4GeV.npy"), np.load("0.984cut_flag_4GeV.npy"), np.load("momenta_4GeV_nocut.npy")
# print(flag_984.shape)
# print(flag_939.shape)
#
# filtered_939 = np.zeros(shape=(70825,28))
# filtered_984 = np.zeros(shape=(35139,28))
# n = 0
# m = 0
# for i in range(momenta.shape[0]):
#     if flag_939[i]:
#         filtered_939[n] = np.hstack((momenta[i], ob[i]))
#         n += 1
#     if flag_984[i]:
#         filtered_984[m] = np.hstack((momenta[i],ob[i]))
#         m += 1
# print(filtered_984[:10])
# print(filtered_939[-10:])
# np.save("filtered984",filtered_984)
# np.save("filtered939",filtered_939)
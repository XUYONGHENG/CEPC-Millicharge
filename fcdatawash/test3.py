import numpy as np
import cut as cut
import matplotlib.pyplot as plt


def gf(mz,mf,nc,c):
    # print(mz,mf,nc,c)
    return nc * c**2 * np.sqrt(0.25*mz**2-mf**2) * (mz**2 + mf**2) / (6*np.pi*mz**2)

def decay_width(mass,epsilon):
    if mass/2 < 1.28:
        w0 = gf(mass,0,3,2/3)+2*gf(mass,0,3,-1/3)+2*gf(mass,0,1,-1)
    elif 1.28 <= (mass/2) <1.78:
        w0 =  gf(mass,0,3,2/3)+2*gf(mass,0,3,-1/3)+2*gf(mass,0,1,-1) + gf(mass,1.28,3,2/3)
    elif 1.78<= (mass/2) < 4.18:
        w0 = 2*gf(mass,0,3,2/3)+2*gf(mass,0,3,-1/3)+2*gf(mass,0,1,-1) + gf(mass,1.28,3,2/3) + gf(mass,1.78,1,-1)
    else:
        w0 =  gf(mass,0,3,2/3)+2*gf(mass,0,3,-1/3)+2*gf(mass,0,1,-1) + gf(mass,1.28,3,2/3) + gf(mass,1.78,1,-1) + gf(mass,4.18,3,-1/3)

    return epsilon**2*w0

# print(gf(100,0,1,1))
# print(decay_width(100,0.01))
# print(1e-4*gf(100,0,1,1)/decay_width(100,1e-2))
# a = np.load('/store/disposed/dfbgzd.npy')
# print(np.sum(a[:,-1]))
# print(a[0])

# a = np.load('/store/disposed/ee240_107d.npy')
# am,aw =np.column_stack((a[:,0],a[:,2])),a[:,-1]
# np.savetxt('plotCSV/ee240_107.csv',am,delimiter=', ')
# np.savetxt('plotCSV/ee240_107w.csv',aw,delimiter=', ')

# mass = 10**np.linspace(0,2,21)
# for i in range(21):
#     print(i,mass[i])

# print(decay_width(mass=150,epsilon=0.01))
# dots = 10**np.linspace(-3,0,31)
# for i in range(31):
#     print(528.5*(0.745*1e-4*dots[i]**2)/(18*1e-4+0.745*dots[i]**2))
# a,b = np.load('/home/xyh/Desktop/zydata/sbdotscepcdfh.npy'),\
#       np.load('/home/xyh/Desktop/zydata/crosssections_fig12_left.npy')
# print(np.hstack((a,b[:,1:])))
# np.save('/home/xyh/Desktop/zydata/sbdotscepcdfh.npy',np.hstack((a,b[:,1:])))
# print(np.load('/home/xyh/Desktop/zydata/sbdotscepcdfh.npy').shape)

# a = np.load('plotformalCSV/xsectionscepcdfh_iv_add3.npy')
# b = np.load('plotformalCSV/sbdotscepcdfh_iv_add3.npy')
# c = np.hstack((b,a[:,1:]))
# cc = np.array([75,0.0005759582091546263,0.12913114,0.2293696])
# ccc = np.vstack((c[:100],cc,c[100:]))
# print(ccc)
# np.save('/home/xyh/Desktop/cepcdfh_iv_add.npy',ccc)
# print
# data=np.load('/store/disposed/dfbgd.npy')

# data=np.load('/store/disposed/darkphoton_visiblebg_mumuad.npy')
# print(np.sum(data[:,-1]))
# b, a = np.load('/store/disposed/vmvmcepc3d.npy'), np.load('/store/disposed/vevecepc3d.npy')
# b[:, -1] = 2 * b[:, -1]
# ivbg = np.vstack((a, b))
# data = ivbg
# a,edges = np.histogram(a=data[:,0],bins=120,weights=data[:,-1],normed=False)
# print(a)
b, a = np.load('/store/disposed/vmvmcepc3d.npy'), np.load('/store/disposed/vevecepc3d.npy')
# np.savetxt('plotCSV/vevecepc3d.csv',a,delimiter=', ')
# np.savetxt('plotCSV/vmvmcepc3d.csv',b,delimiter=', ')
b[:, -1] = 2 * b[:, -1]
ivbg = np.vstack((a, b))
# print(ivbg.shape)

hist,edges = np.histogram(a=ivbg[:,0],bins=200,range=(1,120),weights=ivbg[:,4])
print(hist.shape)
histdata = np.zeros(shape=(200))
for i in range(200):
    histdata[i] = (edges[i]+edges[i+1])/2
print(histdata.shape)

fig,ax = plt.subplots()
ax.hist(x=histdata, bins=edges, weights=hist, \
         label="$defaultset$", histtype="step", rwidth=1.0, \
         color="#5954d8", edgecolor='red', linewidth=3, linestyle="solid", \
         bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")
# ax.set_yscale('log')
plt.show()
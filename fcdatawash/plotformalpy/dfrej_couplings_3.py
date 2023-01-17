import matplotlib.pyplot as plt
import numpy as np


lamb = 5.39412e6*0.535
dotsiv,dotsv = np.zeros(shape=(100000,2)),np.zeros(shape=(100000,2))
gvxs = 10 ** np.linspace(-3, 0, 100000)


dots_dominate = np.zeros_like(dotsiv)
dots_dominate[:,0] = gvxs
dots_dominate[:,1] = gvxs*1.518

dotsiv[:,0],dotsv[:,0] = gvxs,gvxs
def gvf_f(x):
    return (lamb-18/(0.745*x**2))**(-0.5)


def gvfv_f(x):
    # return np.sqrt(1.5645e-12*(1.59948e6+94.2656*np.sqrt(2.8796e8+9.52e12*x**2)))
    # return np.sqrt(5.6255e-13*(3.1167e6+131.586*np.sqrt(5.61e8+2.64e13*x**2)))
    return np.sqrt(1.09e-13*(1.22e7+592*np.sqrt(4.54e8+2.74e13*x)))



def ssiv(x,f):
    return (x**2*f**2)/(8*f**2+x**2)*lamb


def ssv(x,f):
    return f**4/(8*f**2+x**2)*8690050



dotsiv[:,1],dotsv[:,1] = gvf_f(dotsiv[:,0]),gvfv_f(dotsv[:,0])
nans = np.isnan(dotsiv)
# print(nans)
dotsiv[nans] = 1

# plt.imshow(contour2)
# plt.show()
# print(dotsiv[-100:])
# for i in range(100000):
#     gvx = gvxs[i]
#     print(i,lamb/2-8/(i**2),(lamb/2-8/(i**2))**(-0.5))
    # gvf = (lamb/2-8/(gvx**2))**(-0.5)
    # gvfv = np.sqrt(1.291e-12*(719751+848.381*np.sqrt(719751+1.54925e12*gvx**2)))
    # dotsiv[i],dotsv[i] = np.array([gvxs[i],gvf]),np.array([gvxs[i],gvfv])

# for i in range(100000):
#     if dotsv[i,1]<dotsiv[i,1] and dotsv[i+1,1]>dotsiv[i+1,1]:
#         print(i)
#         continue

fig,ax = plt.subplots(figsize=(12,9))
l1, = ax.plot(dotsiv[:,0],dotsiv[:,1],linewidth=3,color='blue')
l2, = ax.plot(dotsv[:,0],dotsv[:,1],linewidth=3,color='red',linestyle='dashed')
# l3, = ax.plot(a[:,0],a[:,1])
l4, = ax.plot(dots_dominate[:,0],dots_dominate[:,1],linewidth=0)

# print(dotsv[14607])

ax.fill_between(gvxs[:],np.append(dotsv[:15601,1],dots_dominate[15601:,1]),y2=10,alpha=0.5,color='red')
# ax.fill_between(gvxs[14708:],y2=10,alpha=0.5,color='red')
ax.fill_between(gvxs[15602:],dotsiv[15602:,1],dots_dominate[15602:,1],alpha=0.5,color='blue')


# ax.fill_between(dotsv[:14607,0],dotsv[:,14607,1],dotsiv[:14607,1])
ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'$g_\chi^V$',fontsize=25)
ax.set_ylabel(r'$g_f^V$',fontsize=25)

ax.tick_params(which = 'major', length=8,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)

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

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.set_xlim(1e-3,1)
ax.set_ylim(1e-4,1e-1)
# ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)


ax.text(1e-1,9e-3,r'$\mu^+\mu^-\gamma$',fontsize=25,color='red',rotation=13.5)
ax.text(1e-1,1.2e-3,r'$\bar{\chi}\chi\gamma$',fontsize=25,color='blue')

ax.text(8e-3,3e-4,r'CEPC sensitivity',fontsize=25)

ax.text(1.5e-3,1.7e-4,r'$\sqrt{s}=240$ GeV $g^A=0,m_\chi=50$ GeV, $m_{Z^\prime}=150$ GeV',fontsize=25)


plt.savefig('../figformal/dfrej_couplings3.pdf',format='pdf')

plt.show()
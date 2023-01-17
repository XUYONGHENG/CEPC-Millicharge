import numpy as np
import matplotlib.pyplot as plt

dotright = np.array([0.0010172, 0.00106967, 0.00121307, 0.00135895, 0.00146038, \
0.00154349, 0.0016144, 0.00167725, 0.00173103, 0.00178249, \
0.00182901, 0.00187237, 0.00191119, 0.00194868, 0.00198499, \
0.00201867, 0.00205091, 0.00208216, 0.00211234, 0.00214132, \
0.00216863, 0.00219493, 0.0022197, 0.0022433, 0.00226665, 0.00228984, \
0.00231352, 0.00233537, 0.00235569, 0.00237727, 0.00239677, \
0.00241637, 0.00243549, 0.00245317, 0.0024704, 0.00248752, \
0.00250457, 0.00252022, 0.00253754, 0.00255349, 0.0025698, \
0.00258439, 0.00260079, 0.00261298, 0.002627, 0.00264184, 0.00265752, \
0.00267224, 0.00268448, 0.00269647, 0.00270972, 0.00272199, \
0.00273519, 0.00274781, 0.00275826, 0.00277047, 0.00278408, \
0.00279352, 0.00280477, 0.00281544, 0.0028251, 0.00283416, \
0.00284553, 0.00285633, 0.00286741, 0.00287749, 0.00288828, \
0.00289678, 0.00290642, 0.00291592, 0.00292528, 0.00293539, \
0.00294405, 0.00295302, 0.00296141, 0.00297195, 0.00298102, \
0.00299181, 0.00299974, 0.00300754, 0.00301194, 0.00301996, \
0.00302739, 0.00303375, 0.00304047, 0.00304805, 0.00305504, \
0.00306142, 0.00306719, 0.00307335, 0.00307788, 0.00308686, \
0.00309424, 0.00309998, 0.00310459, 0.00310907, 0.00311449, \
0.00312247, 0.00313037, 0.00313606])
dotright2 = np.zeros(shape=(100,2))
dotright2[:,0],dotright2[:,1] = 75.01 + np.linspace(0,1,100,endpoint=False),dotright

dot75 = np.array([75.0,4e-5])

dotleft = np.array([0.000520233, 0.000520175, 0.000520117, 0.000520059, 0.00052, \
0.000519941, 0.000519882, 0.000519822, 0.000519762, 0.000519702, \
0.000519641, 0.00051958, 0.000519519, 0.000519457, 0.000519395, \
0.000519333, 0.00051927, 0.000519206, 0.000519142, 0.000519078, \
0.000519013, 0.000518948, 0.000518882, 0.000518815, 0.000518748, \
0.00051868, 0.000518612, 0.000518542, 0.000518473, 0.000518402, \
0.000518331, 0.000518259, 0.000518186, 0.000518112, 0.000518037, \
0.000517961, 0.000517884, 0.000517806, 0.000517727, 0.000517647, \
0.000517566, 0.000517483, 0.000517399, 0.000517313, 0.000517226, \
0.000517137, 0.000517046, 0.000516954, 0.000516859, 0.000516763, \
0.000516664, 0.000516563, 0.000516459, 0.000516353, 0.000516244, \
0.000516132, 0.000516016, 0.000515897, 0.000515775, 0.000515648, \
0.000515516, 0.00051538, 0.000515239, 0.000515093, 0.00051494, \
0.00051478, 0.000514614, 0.00051444, 0.000514257, 0.000514064, \
0.000513861, 0.000513647, 0.00051342, 0.000513178, 0.000512921, \
0.000512646, 0.00051235, 0.000512033, 0.000511689, 0.000511316, \
0.000510909, 0.000510463, 0.000509972, 0.000509428, 0.00050882, \
0.000508138, 0.000507366, 0.000506483, 0.000505465, 0.000504276, \
0.00050287, 0.000501182, 0.000499117, 0.000496535, 0.000493214, \
0.000488793, 0.000482621, 0.000473406, 0.000458122, 0.000427069])
dotleft2 = np.zeros(shape=(100,2))
dotleft2[:,0],dotleft2[:,1] = 74.0 + np.linspace(0,1,100,endpoint=False),dotleft

dots = np.vstack((dotleft2,dot75,dotright2))

fig,ax = plt.subplots(figsize=(12,9))
ax.plot(dots[:,0],dots[:,1],linewidth=3)

ax.set_xlim((74,76))
ax.set_ylim((1e-5,5e-2))

# ax.set_xscale('log')
ax.set_yscale('log')


ax.tick_params(which = 'major', length=8,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)
ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax.set_ylabel(r'$g_f^V$',fontsize=25)
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
#
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

# xmajorLocator = plt.MultipleLocator(5)
# ax.xaxis.set_major_locator(xmajorLocator)
xminorLocator = plt.MultipleLocator(1)
ax.xaxis.set_minor_locator(xminorLocator)
ax.ticklabel_format(axis='x',style='plain')
# ax.set_xticklabels([74,74.5,75,75.5,76], fontdict=None, minor=False)

# plt.xticks(myxticks)
plt.savefig('../figformal/dfrej_3_zoomin.pdf',format='pdf')
plt.show()

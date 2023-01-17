import numpy as np
import cut as cut
import tools as tools

masses = np.linspace(50,100,201,endpoint=False)
print(masses[101])
a = np.load('/store/disposed/finalpush/zp/h/a/mz150a_mx102_50-100.lhed.npy')
print(np.sum(a[:,-1]))
import numpy as np
import matplotlib.pyplot as plt
import os as os
import re as re
import time as time

print('Shit!')

pattern = re.compile(r'\d+\.\d+',re.I)

def pytail(command):
    a = os.popen(command)
    return a.readlines()


def get_sigma(energy):
    os.system('rm -rf run.uu*')
    os.system('./run uuuuu '+str(energy)+','+str(energy))
    print('Bing!')
    if energy >= 100:
        #只取我们需要的最后8行
        os.system('tail -8 run.uuuuu.00'+str(int(energy))+',00'+str(int(energy))+',00010/0000001 > run.uutmp')
        #读取这个切下来的只有一行的文件中的第一行
        with open('run.uutmp') as file_object:
            read = file_object.readline()
        #返回匹配到的第一个数字.
            return np.float64(pattern.findall(read)[0])
    if 10 <= energy < 100:
        os.system('tail -8 run.uuuuu.000'+str(int(energy))+',000'+str(int(energy))+',00010/0000001 > run.uutmp')
        with open('run.uutmp') as file_object:
            read = file_object.readline()
            return np.float64(pattern.findall(read)[0])

    if 1 <= energy < 10:
        os.system('tail -8 run.uuuuu.0000'+str(int(energy))+',0000'+str(int(energy))+',00010/0000001 > run.uutmp')
        with open('run.uutmp') as file_object:
            read = file_object.readline()
            return np.float64(pattern.findall(read)[0])

if __name__ == '__main__':
    a = np.linspace(1,300,300)
# print(a[:2])
    b = np.zeros_like(a)
    for i in range(b.shape[0]):
        b[i] = get_sigma(energy=a[i])

    np.save('result.npy',np.column_stack((a,b)))
# get_sigma(105)
# print(os.system('ls'))
# with open('run.uutmp') as file_object:
#     read = file_object.readline()
#     print(pattern.findall(read))
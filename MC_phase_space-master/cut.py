import numpy as np

def cut1(p):
    if p[10] > 10 and np.abs(p[-2]) < 0.94:
        if np.abs(p[3]) > 0.939 and np.abs(p[8]) > 0.939:
            return True
    return False

def cut2(p):

    if p[10] > 10 and np.abs(p[-2]) < 0.94:
        if np.abs(p[3]) > 0.984 and np.abs(p[8]) > 0.984:
            return True
    return False

def cut_besiii(p):
    if (np.abs(p[-2]) < 0.8 and p[10] > 0.025) or (0.86 < np.abs(p[-2]) < 0.92 and p[10] >0.05):
        if np.abs(p[3])>0.95 and np.abs(p[8])>0.95:
            return True
    return False

def cut_neutrino(p):
    if p[10] > 10 and np.abs(p[-2]) < 0.939:
        return True
    return False

def cut_3(p):
    if np.abs(p[3]) > 0.95 and np.abs(p[8]) > 0.95:
        return True
    return False

def cut_besiii_4(p):
    if (np.abs(p[-2]) < 0.8 and p[3] > 0.025) or (0.86 < np.abs(p[-2]) < 0.92 and p[3] >0.05):
        if np.abs(p[0])>0.95 and np.abs(p[1])>0.95:
            return True
    return False

def cut_neutrino_besiii_4(p):
    if (np.abs(p[-2]) < 0.8 and p[3] > 0.025) or (0.86 < np.abs(p[-2]) < 0.92 and p[3] >0.05):
        return True
    return False

def cut_4(p):
    if np.abs(p[-2]) > 0.95 and np.abs(p[-1]) > 0.95:
        if p[0] > 0.025 and np.abs(p[1]) < 0.95:
            return True
    return False
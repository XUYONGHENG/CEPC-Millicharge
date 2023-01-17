import numpy as np
import MonteCarlo as mc
import time as time

def event_generator(number_of_events,s_sqrt,savename):
    a = np.zeros(shape=(number_of_events,4))
    for i in range(number_of_events):
        a[i] = mc.two_three_phase_space_dot_rambo(s_sqrt=s_sqrt,masses=[0,0,0])
    np.save("/store/kinematics/p"+savename, a)

start = time.clock()
event_generator(100000,4,"vv2")
end = time.clock()
print(end-start)


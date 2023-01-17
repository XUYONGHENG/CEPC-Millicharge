import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()

circle = plt.Circle((0,0),radius=5,fc='b',alpha=0.6)
circle2 = plt.Circle((6,0),radius=5,fc='g',alpha=0.6)
circle3 = plt.Circle((3,np.sqrt(3)*3),radius=5,fc='r',alpha=0.6)
plt.gca().add_patch(circle)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.text(1.5,1.0,'     Origin of universe\n\n   Unification of forces\n\n         New Physics\n\nBeyond Standard Model'
         ,fontdict={'fontsize':11,'color':'white'})
plt.text(-0.8,3.5,'Matter/Antimatter\n Asymmerty',fontdict={'fontsize':14,'color':'white'})
plt.text(4.5,3.6,'Dark Matter',fontdict={'fontsize':14,'color':'white'})
plt.text(2,7.8,'Origin of Mass',fontdict={'fontsize':14,'color':'white'})
plt.text(2,7.8,'Origin of Mass',fontdict={'fontsize':14,'color':'white'})
plt.text(8,-1,'Dark Energy',fontdict={'fontsize':14,'color':'white'})
plt.text(5.7,-3,'Cosmic Particles',fontdict={'fontsize':14,'color':'white'})
plt.text(-4,-1,'Neutrino Mass',fontdict={'fontsize':14,'color':'white'})
plt.text(-2,-3,'Proton Decay',fontdict={'fontsize':14,'color':'white'})
plt.text(-0.5,10.5,'The Energy Frontier',fontdict={'fontsize':30,'color':'black'})
plt.text(-7,-2,'The intensity Frontier',fontdict={'fontsize':30,'color':'black'},rotation=320)
plt.text(7,-2,'The Cosmic Frontier',fontdict={'fontsize':30,'color':'black'},rotation=40)
plt.axis('scaled')
plt.axis('off')
plt.show()
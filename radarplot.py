import matplotlib as plt
import pandas as pd
import seaborn as sns
import numpy as np
import itertools as it

area = 0

labels=['0 Jet','1 Jet', '2 Jet','a','b','c','d','e','f','g','h','i','j']
misclass= [0.0,0.9,0.8,0.2,0.6,0.7,0.64,0.5,0.3,0.1,0.28,0.8,0.9]
#misclass2 = np.array([0.8,0.2,0.6,0.8,0.8,0.9,0.1,0.9, 0.8, 0.7,0.9])

angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles += np.pi/2 #rotate for niceness

#calculate the area of the subtriangles between axes and sum
for pair in it.combinations(misclass,r=2):
    smolarea = pair[0]*pair[1]*0.5*np.sin(2*np.pi/len(labels))
    area += smolarea

# close the plot or it won't draw one of the lines :(
misclass=np.concatenate((misclass,[misclass[0]]))
#misclass2=np.concatenate((misclass2,[misclass2[0]]))
angles=np.concatenate((angles,[angles[0]]))


fig=sns.plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_ylim(0,1)
ax.plot(angles, misclass, 'o-', linewidth=2, label = 'model1')
#ax.plot(angles, misclass2, 'o-', linewidth=2, label = 'model2')
ax.fill(angles, misclass, alpha=0.25)
#ax.fill(angles, misclass2, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title('Area calculation example cobweb (fake data)')
ax.legend(loc=[-0.1,-0.05])
ax.text(-1.1,1.2,'Area: %f' % (area))

ax.grid(True)

print 'Area:', area
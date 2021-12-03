import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw=RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig ,ax=plt.subplots()

ax.scatter(rw.x_values,rw.y_values,c=rw.y_values,cmap=plt.cm.Reds,s=10)

plt.show()

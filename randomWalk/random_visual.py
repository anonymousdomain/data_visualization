import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw=RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig ,ax=plt.subplots()
point_nums=range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,c=point_nums,cmap=plt.cm.Blues,edgecolors='none',s=10)

#plt.show();
plt.savefig('img\\random_walk.png',bbox_inches='tight')
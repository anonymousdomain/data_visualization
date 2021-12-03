import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw=RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig ,ax=plt.subplots()
point_nums=range(rw.num_points)
ax.scatter(0,0,c='red',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolors='none',s=100)
ax.scatter(rw.x_values,rw.y_values,c=point_nums,cmap=plt.cm.Blues,edgecolors='none',s=10)
#get rid of the axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show();
#plt.savefig('img\\random_walk.png',bbox_inches='tight')
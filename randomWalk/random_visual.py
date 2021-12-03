import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use('classic')

fig, ax = plt.subplots(figsize=(8, 8))
point_nums = range(rw.num_points)
ax.scatter(0, 0, c='red', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1],
           c='black', edgecolors='none', s=100)
# ax.plot(rw.x_values,rw.y_values,linewidth=1)
ax.scatter(rw.x_values, rw.y_values, c=point_nums,
           cmap=plt.cm.Blues, edgecolors='none', s=1)
# get rid of the axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
# plt.savefig('img\\random_walk.png',bbox_inches='tight')

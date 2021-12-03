import matplotlib.pyplot as plt

inputs=range(1,1001)
values=[x**3 for x in inputs]
#add style
plt.style.use('seaborn')

fig,ax=plt.subplots()
ax.scatter(inputs,values,c=values,cmap=plt.cm.Blues,s=5)

#set title
ax.set_title('square_numbers',fontsize=24)
ax.set_xlabel('values',fontsize=14)
ax.set_ylabel('square values',fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=10)
#expand the axis x from 0 to 1100 and y from 0to 1100000
ax.axis([0,1100,0,1100000])
plt.savefig('img\cubics_scatter.png',bbox_inches='tight')




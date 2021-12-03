import matplotlib.pyplot as plt
#add style
plt.style.use('seaborn')

fig,ax=plt.subplots()
ax.scatter(2,4,s=100)

#set title
ax.set_title('square_numbers',fontsize=24)
ax.set_xlabel('values',fontsize=14)
ax.set_ylabel('square values',fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)
plt.show()
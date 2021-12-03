import matplotlib.pyplot as plt

inputs=[1,2,3,4,5]
squares=[1,4,9,16,25]

fig ,ax=plt.subplots()
ax.plot(inputs,squares,linewidth=2)

#set chart title 
ax.set_title("square Numbers",fontsize=24)
ax.set_xlabel("values",fontsize=14)
ax.set_ylabel("square of values",fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()
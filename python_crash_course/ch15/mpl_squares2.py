from matplotlib import pyplot as plt

squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares,linewidth=3)
ax.set_title("Square Number",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Value Squared",fontsize=14)
ax.tick_params(axis="both",labelsize=14)
plt.savefig("plot2.png")

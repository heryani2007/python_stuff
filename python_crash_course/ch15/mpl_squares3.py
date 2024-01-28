from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_ylabel("Whole")
ax.set_xlabel("Whole")
ax.set_title("title")
plt.savefig("plot3.png")

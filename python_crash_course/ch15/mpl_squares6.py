import matplotlib.pyplot as plt

x = range(1,1001)
y = []
for number in x:
    y.append(number**2)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x,y,c=y,cmap=plt.cm.Blues,s=10)
ax.axis([0, 1100, 0, 1100000])
plt.savefig("plot7.png",bbox_inches="tight")

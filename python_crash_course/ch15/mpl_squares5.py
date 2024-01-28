import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_title("Squares")
ax.set_ylabel("Dependent")
ax.set_xlabel("Independent")
plt.savefig("plot5.png")

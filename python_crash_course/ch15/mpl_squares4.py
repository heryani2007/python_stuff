import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")
fog, ax = plt.subplots()

ax.scatter(2,5,s=100)
plt.savefig("plot4.png")

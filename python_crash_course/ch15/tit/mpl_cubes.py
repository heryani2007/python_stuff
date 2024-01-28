import matplotlib.pyplot as plt
x_values = range(1,5000)
y_values = []
for num in x_values:
    y_values.append(num**3)

fig, ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
ax.set_title("Sample")
ax.set_xlabel("x-value")
ax.set_ylabel("y-value")

plt.savefig("plot.png")

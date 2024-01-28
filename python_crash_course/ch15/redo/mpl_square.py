import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = []

for num in x_values:
	y_values.append(num**2)

fig, ax = plt.subplots()
ax.set_title("sample title")
ax.set_xlabel("x-value")
ax.set_ylabel("y-value")
ax.scatter(x_values,y_values, c="red", s = 5)
plt.savefig("plot.png")

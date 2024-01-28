import matplotlib.pyplot as plt
from random_walk import Randomwalk

rw = Randomwalk()
rw.walk()

for _ in range(3):
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    plt.savefig("rw_plot.png")

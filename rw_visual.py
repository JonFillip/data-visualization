from random_walks import RandomWalk
import matplotlib.pyplot as plt

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()
# Plot the points in the walk as a scatter plot.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=10)


if __name__ == '__main__':
    plt.show()

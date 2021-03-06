from random_walk.random_walks import RandomWalk
import matplotlib.pyplot as plt

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()
    # Plot the points in the walk as a scatter plot.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_number, edgecolors='none',
               cmap=plt.cm.Blues, s=10)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

from molecular_motion import MolecularMotion
import matplotlib.pyplot as plt

# Keep making new walks, as long as the program is active.
while True:
    # Make random motion.
    mm = MolecularMotion(5000)
    mm.fill_path()
    # Plot the points of the grain's path as a scatter plot.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_number = range(mm.num_points)
    ax.plot(mm.x_values, mm.y_values, linewidth=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(mm.x_values[-1], mm.y_values[-1], c='red', edgecolors='none',
               s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

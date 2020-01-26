import matplotlib.pyplot as plt

"""
15-1. Cubes: Plot the first five cubic numbers, and then plot the first 5000 cubic numbers. Apply a colormap to the plot 
"""
cube_values = range(1, 500)
cubed_values = [x ** 3 for x in cube_values]

# Select graph styling.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Initiate scatter plot function
ax.scatter(cube_values, cubed_values, c=cubed_values, cmap='BuPu', s=10)

# Setting title and labels for the graph.
ax.set_title("Cube of Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube of values", fontsize=14)

# Set size of the tick label
ax.tick_params(axis='both', which='major', labelsize=14)

# Set a range for each axis
ax.axis([0, 550, 0, 150000000])

if __name__ == "__main__":
    plt.savefig('cubic_plot.png', bbox_inches='tight')
    plt.show()

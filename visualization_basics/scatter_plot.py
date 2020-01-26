import matplotlib.pyplot as plt

squares = range(1, 1000, 10)
value_root = [x ** 2 for x in squares]
# Select graph styling
plt.style.use("seaborn")
fig, ax = plt.subplots()
# Initiate scatter plot function
ax.scatter(squares, value_root, c=value_root, cmap='Greens', s=10)

# Set the title and labels for the graph
ax.set_title("Square of Number", fontsize=24)
ax.set_xlabel("Root of Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick label.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set a range for each axis.
ax.axis([0, 1100, 0, 1100000])

if __name__ == "__main__":
    plt.savefig('square_scatterplot.png', bbox_inches='tight')  # To
    # automatically save plots
    plt.show()

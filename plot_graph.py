import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
value_root = [1, 2, 3, 4, 5]
plt.style.use("seaborn-darkgrid")
fig, ax = plt.subplots()
# Change the thickness of the graph line
ax.plot(value_root, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Root of Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(axis="both", labelsize=14)

if __name__ == "__main__":
    plt.show()

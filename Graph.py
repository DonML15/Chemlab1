#This code produces the bar graph for the measurements in the measurements lab.

import numpy as np
import matplotlib.pyplot as plt

# Density measurements (g/mL)
densities = np.array([0.895, 0.958, 0.968, 0.972, 0.984])

# Calculate average and sample standard deviation
average = np.mean(densities)
standard_deviation = np.std(densities, ddof=1)

# True density (g/mL)
true_density = 1.000

# Measurement labels
measurements = [
    "Measurement 1",
    "Measurement 2",
    "Measurement 3",
    "Measurement 4",
    "Measurement 5"
]

# Create the bar graph
plt.figure(figsize=(10, 6))

plt.bar(
    measurements,
    densities,
    yerr=standard_deviation,
    capsize=5,
    color="steelblue",
    edgecolor="black",
    label="Measured density"
)

# Average density line
plt.axhline(
    average,
    color="orange",
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.4f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label="True density = 1.000 g/mL"
)

# Labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density Measurements (With Graduated Cylinder)")

# Set a reasonable y-axis range
plt.ylim(0.85, 1.05)

# Show legend and grid
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.5)

plt.tight_layout()
plt.show()

# Print the calculated values
print(f"Average density: {average:.4f} g/mL")
print(f"Standard deviation: {standard_deviation:.4f} g/mL")

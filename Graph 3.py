import matplotlib.pyplot as plt
import numpy as np

# Density measurements
densities = [8.8, 6.4, 6.3, 6.3]

# Measurement numbers
measurements = [1, 2, 3, 4]

# Accepted value, average, and standard deviation
accepted_value = 7.18
average_value = 6.9
standard_deviation = 1.24

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    measurements,
    densities,
    yerr=standard_deviation,
    capsize=5
)

# Accepted value line
plt.axhline(
    accepted_value,
    linestyle="--",
    label="Accepted Value = 7.18 g/cm³"
)

# Average value line
plt.axhline(
    average_value,
    linestyle="-.",
    label="Average = 6.9 g/cm³"
)

# Axis labels
plt.xlabel("measurements")
plt.ylabel("Density (g/cm³)")

# Measurement labels
plt.xticks(
    measurements,
    ["Measurement 1", "Measurement 2", "Measurement 3", "Measurement 4"]
)

# Y-axis range
plt.ylim(0, 10)

# Add legend
plt.legend()

# Show chart
plt.tight_layout()
plt.show()
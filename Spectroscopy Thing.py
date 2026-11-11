import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Helium spectroscope calibration data

# Three scale readings for each spectral line
reading1 = np.array([4.50, 4.70, 4.90, 5.80, 6.50, 6.909])
reading2 = np.array([4.70, 4.80, 5.00, 5.80, 6.50, 6.90])
reading3 = np.array([4.50, 4.70, 4.95, 5.70, 6.50, 7.00])

# Calculate the average scale reading for each line
scale_reading = (reading1 + reading2 + reading3) / 3

# Corresponding known helium wavelengths, in nanometers
wavelength = np.array([447, 470, 492, 588, 668, 707])

# Calculate the linear regression
slope, intercept, r_value, p_value, std_err = linregress(
    scale_reading, wavelength
)

# Create points for drawing a smooth regression line
x_line = np.linspace(scale_reading.min(), scale_reading.max(), 100)
y_line = slope * x_line + intercept

# Print the averages and regression results
print("Average scale readings:")
for i, value in enumerate(scale_reading, start=1):
    print(f"Line {i}: {value:.4f}")

print()
print(f"Regression equation: wavelength = {slope:.4f}(scale reading) "
      f"+ ({intercept:.4f})")
print(f"R = {r_value:.4f}")
print(f"R-squared = {r_value**2:.4f}")

# Plot the measured data and regression line
plt.figure(figsize=(9, 6))
plt.scatter(
    scale_reading,
    wavelength,
    label="Helium spectral lines",
    marker="o"
)
plt.plot(
    x_line,
    y_line,
    label="Linear regression"
)

# Add the regression equation and R-squared value to the graph
equation_text = (
    f"y = {slope:.4f}x {intercept:+.4f}\n"
    f"R² = {r_value**2:.4f}"
)
plt.text(
    0.05,
    0.95,
    equation_text,
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

plt.title("Helium Spectroscope Calibration")
plt.xlabel("Scale Reading")
plt.ylabel("Wavelength (nm)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the graph
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('stars.csv')  # Must contain 'Temperature' and 'Luminosity' columns

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Luminosity'], c='skyblue', edgecolors='black', s=40)
plt.gca().invert_xaxis()
plt.xlabel("Temperature (K)")
plt.ylabel("Luminosity (L☉)")
plt.title("Hertzsprung-Russell Diagram")
plt.grid(True)

# Save plot
plt.savefig("hr_diagram.png", dpi=300)
plt.show()
print("H-R diagram saved as hr_diagram.png")
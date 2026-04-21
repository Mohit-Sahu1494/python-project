# Q31. Write a program combining numpy, pandas, and matplotlib for simple data analysis.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Use Numpy to generate some random data
np.random.seed(42) # For reproducibility
days = np.arange(1, 31) # 1 to 30 days
temperature = np.random.normal(loc=25, scale=5, size=30) # Mean 25, Std 5
humidity = np.random.normal(loc=60, scale=10, size=30)

# 2. Use Pandas to create a DataFrame and perform basic analysis
data = {
    'Day': days,
    'Temperature_C': temperature,
    'Humidity_Percent': humidity
}
df = pd.DataFrame(data)

print("--- Data Summary ---")
print(df.describe())

# Add a rolling average column for smooth trend using Pandas
df['Temp_Rolling_Avg'] = df['Temperature_C'].rolling(window=5).mean()

# 3. Use Matplotlib to visualize the data
plt.figure(figsize=(10, 6))

# Plot daily temperature
plt.plot(df['Day'], df['Temperature_C'], label='Daily Temperature', color='lightblue', marker='o', alpha=0.7)

# Plot rolling average
plt.plot(df['Day'], df['Temp_Rolling_Avg'], label='5-Day Rolling Avg Temp', color='red', linewidth=2)

plt.title('30-Day Temperature Analysis')
plt.xlabel('Day of Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

plt.savefig("q31_analysis_plot.png")
print("\nPlot saved successfully as 'q31_analysis_plot.png'")
# plt.show() # Uncomment to view interactively

import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Total': [8625.62, 7646.14, 7269.93, 6462.09, 4764.7, 4133.77, 4976.58, 9964.66, 9965.35, 4463.35, 4047.44, 3853.35, 4445.63, 3980.99, 3767.74, 3942.93, 5100.33, 4302.04, 4302.6],
    'Area': [497.5, 1215.5, 901, 515, 1399.5, 911.5, 440, 354.5, 314, 638, 684, 1192, 493.5, 732, 1421, 1097, 448, 610, 665.5],
    'WNS': [0.257, -1, -0.862, 0.024, -2.788, 0.068, 0.014, 0.174, 0.141, 0.078, 0.062, -1.2, 0.014, 0.047, -2.307, -1.685, 0.031, 0.088, 0.023]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color column based on WNS and Area
df['color'] = 'green'  # Default to green
df.loc[df['WNS'] < 0, 'color'] = 'red'  # Negative WNS are red
df.loc[df['Area'].isin([440, 493.5, 448]), 'color'] = 'pink'  # Highlight specific areas

# Plot
plt.figure(figsize=[10, 6])
plt.scatter(df['Total'], df['Area'], c=df['color'])
plt.xlabel('Total (Million Clock Cycles)')
plt.ylabel('Area')
plt.title('Scatter Plot of Total Clock Cycles vs Area (colored by WNS)')
plt.grid(True)

plt.show()

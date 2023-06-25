# import pandas as pd
# import matplotlib.pyplot as plt

# # Data
# data = {
#     'clock': [70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 72, 72, 73, 73],
#     'Area': [447.5, 452, 465, 474, 453, 458, 443.5, 444, 441.5, 443, 395.5, 374.5, 540.5, 550.5, 570, 496.5, 544.5, 545.5, 575, 578.5, 574.5, 541.5],
#     'total': [9126.052, 8074.744, 7860.416, 7860.56, 7138.743, 7187.061, 7138.874, 7138.554, 7145.513, 7138.521, 9779.958, 12703.994, 4728.968, 4195.659, 4127.829, 4939.991, 4195.794, 4127.413, 4159.436, 4238.207, 4159.61, 4159.52]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Create a color column based on clock
# color_dict = {70: 'blue', 71: 'green', 72: 'red', 73: 'pink'}  # Define colors for each clock value
# df['color'] = df['clock'].map(color_dict)  # Create color column

# # Plot
# plt.figure(figsize=[10, 6])
# plt.scatter(df['total'], df['Area'], c=df['color'])
# plt.xlabel('Total')
# plt.ylabel('Area')
# plt.title('Scatter Plot of Total vs Area (colored by Clock)')
# plt.grid(True)

# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Data 1
data1 = {
    'clock': [70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 72, 72, 73, 73,
              73, 74, 75, 76, 77], # new clock data appended
    'Area': [447.5, 452, 465, 474, 453, 458, 443.5, 444, 441.5, 443, 395.5, 374.5, 540.5, 550.5, 570, 496.5, 544.5, 545.5, 575, 578.5, 574.5, 541.5,
             541.5, 566, 573, 556, 592.5], # new Area data appended
    'total': [9126.052, 8074.744, 7860.416, 7860.56, 7138.743, 7187.061, 7138.874, 7138.554, 7145.513, 7138.521, 9779.958, 12703.994, 4728.968, 4195.659, 4127.829, 4939.991, 4195.794, 4127.413, 4159.436, 4238.207, 4159.61, 4159.52,
             4159.52, 4162.636, 4164.184, 4162.694, 4162.8] # new total data appended
}

# Data 2
data2 = {
    'total': [8625.62, 7646.14, 7269.93, 6462.09, 4764.7, 4133.77, 4976.58, 9964.66, 9965.35, 4463.35, 4047.44, 3853.35, 4445.63, 3980.99, 3767.74, 3942.93, 5100.33, 4302.04, 4302.6],
    'Area': [497.5, 1215.5, 901, 515, 1399.5, 911.5, 440, 354.5, 314, 638, 684, 1192, 493.5, 732, 1421, 1097, 448, 610, 665.5],
    'WNS': [0.257, -1, -0.862, 0.024, -2.788, 0.068, 0.014, 0.174, 0.141, 0.078, 0.062, -1.2, 0.014, 0.047, -2.307, -1.685, 0.031, 0.088, 0.023]
}

# Baseline
baseline = {'total': 8654.753342, 'Area': 492, 'clock': 59}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Calculate execution time in seconds
df1['Time'] = df1['total'] / df1['clock']  # dataset1 time = total/clock frequency
df2['Time'] = df2['total'] / 57.1  # dataset2 time = total/57.1MHz


# Update color dictionary for dataset 1
color_dict1 = {70: 'blue', 71: 'green', 72: 'red', 73: 'pink', 74: 'purple', 75: 'orange', 76: 'yellow', 77: 'brown'}
df1['color'] = df1['clock'].map(color_dict1)

# Define colors and labels for crosses based on 'Area'
colors_crosses = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
special_areas = [497.5, 440, 493.5, 448]
labels_crosses = [f'Area {a}' for a in special_areas] + ['WNS Positive', 'WNS Negative']
df2['color'] = 'blue'  # default color

# Assign colors to specific areas and WNS values
for idx, area in enumerate(special_areas):
    df2.loc[df2['Area'] == area, 'color'] = colors_crosses[idx]

df2.loc[df2['WNS'] < 0, 'color'] = 'red'
df2.loc[df2['WNS'] >= 0, 'color'] = 'green'

# Plot
plt.figure(figsize=[10, 6])

# Plot df1 data as dots with post-design labels
for clock in color_dict1.keys():
    plt.scatter(df1[df1['clock'] == clock]['Time'], df1[df1['clock'] == clock]['Area'], c=color_dict1[clock], marker='o', label=f'Clock {clock}MHz (Post-design)')

# Plot df2 data as crosses with pre-design labels
plt.scatter(df2[df2['WNS'] >= 0]['Time'], df2[df2['WNS'] >= 0]['Area'], c='green', marker='x', label='Positive WNS (Pre-design)')
plt.scatter(df2[df2['WNS'] < 0]['Time'], df2[df2['WNS'] < 0]['Area'], c='red', marker='x', label='Negative WNS (Pre-design)')


# Add the baseline point
baseline_time = baseline['total'] / baseline['clock']
plt.scatter(baseline_time, baseline['Area'], c='black', marker='*', s=200, label='Baseline')

plt.xlabel('Execution Time (s)')
plt.ylabel('Area')
plt.title('Scatter Plot of Execution Time vs Area')
plt.grid(True)
plt.legend()

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Synthesis Strategy': ['Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry'],
    'Implementation Strategy': ['Default', 'Auto_1', 'Auto_2', 'Auto_3', 'Performance_Explore', 'Performance_ExplorePostRoutePhysOpt', 'Performance_ExploreWithRemap', 'Performance_WLBlockPlacement', 'Performance_WLBlockPlacementFanoutOpt', 'Performance_EarlyBlockPlacement'],
    'WNS': [-0.22, -0.169, -0.169, -0.169, -0.059, 0.257, 0.005, -0.349, -0.196, -0.448]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Replace strategy names with abbreviations in the DataFrame
abbreviations = {
    'Flow_PerfThresholdCarry': 'FPTC',
    'Default': 'Dft',
    'Auto_1': 'A1',
    'Auto_2': 'A2',
    'Auto_3': 'A3',
    'Performance_Explore': 'PE',
    'Performance_ExplorePostRoutePhysOpt': 'PE_PRPO',
    'Performance_ExploreWithRemap': 'PE_WR',
    'Performance_WLBlockPlacement': 'P_WLBP',
    'Performance_WLBlockPlacementFanoutOpt': 'P_WLBPF_Opt',
    'Performance_EarlyBlockPlacement': 'P_EBP'
}
df.replace(abbreviations, inplace=True)

# Create a new column for the combination of Synthesis and Implementation strategies
df['Strategy Combination'] = df['Synthesis Strategy'] + ' / ' + df['Implementation Strategy']

# Sort the DataFrame by WNS in descending order
df.sort_values('WNS', ascending=False, inplace=True)

# Plot
plt.figure(figsize=[10, 6])
bars = plt.barh(df['Strategy Combination'], df['WNS'], color='skyblue')
plt.xlabel('WNS')
plt.ylabel('Strategy Combination')
plt.title('WNS for each Strategy Combination')
plt.gca().invert_yaxis()  # highest WNS on top
plt.grid(axis='x')  # grid only in x direction

# Increase the font size of the y-tick labels
plt.tick_params(axis='y', which='major', labelsize=10)

# Add a description of the abbreviations below the chart
abbreviations_text = ', '.join(f'{k}={v}' for k, v in abbreviations.items())
plt.figtext(0.5, -0.1, 'Abbreviations: ' + abbreviations_text, ha='center', fontsize=10, wrap=True)

plt.show()

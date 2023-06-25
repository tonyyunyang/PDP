import pandas as pd
import matplotlib.pyplot as plt

# New Data
data = {
    'Synthesis Strategy': ['Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry', 'Flow_PerfThresholdCarry'],
    'Implementation Strategy': ['Performance_Explore', 'Performance_ExtraTimingOpt', 'Flow_RuntimeOptimized', 'Flow_RunPostRoutePhysOpt', 'Flow_RunPhysOpt', 'Performance_ExplorePostRoutePhysOpt', 'Performance_NetDelay_Low'],
    'WNS': [0.091, 0.091, 0.092, 0.54, 0.54, 0.543, 0.058]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Replace strategy names with abbreviations in the DataFrame
abbreviations = {
    'Flow_PerfThresholdCarry': 'FPTC',
    'Performance_Explore': 'PE',
    'Performance_ExplorePostRoutePhysOpt': 'PE_PRPO',
    'Flow_RuntimeOptimized': 'FRO',
    'Flow_RunPostRoutePhysOpt': 'FR_PRPO',
    'Flow_RunPhysOpt': 'FR_PO',
    'Performance_ExtraTimingOpt': 'PE_TO',
    'Performance_NetDelay_Low': 'P_NDL'
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

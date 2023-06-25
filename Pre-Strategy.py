import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Synthesis Strategy': ['Default', 'Flow_AreaOpt_high', 'Flow_AreaOpt_medium', 'Flow_AreaMultThresholdDSP', 'Flow_AlternateRoutability', 'Flow_PerfOptimized_high', 'Flow_PerfThresholdCarry', 'Flow_RuntimeOptimized'],
    'Implementation Strategy': ['Default', 'Default', 'Default', 'Default', 'Default', 'Default', 'Default', 'Default'],
    'WNS': [-1.122, -1.352, -1.673, -1.122, -1.64, -0.56, -0.22, -1.334]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Replace strategy names with abbreviations in the DataFrame
abbreviations = {
    'Default': 'Dft',
    'Flow_AreaOpt_high': 'FAO_H',
    'Flow_AreaOpt_medium': 'FAO_M',
    'Flow_AreaMultThresholdDSP': 'FAMT_DSP',
    'Flow_AlternateRoutability': 'FAR',
    'Flow_PerfOptimized_high': 'FPO_H',
    'Flow_PerfThresholdCarry': 'FTC',
    'Flow_RuntimeOptimized': 'FRO'
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
plt.figtext(0.5, -0.05, 'Abbreviations: ' + abbreviations_text, ha='center', fontsize=10)

plt.show()

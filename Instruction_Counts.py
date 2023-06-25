import matplotlib.pyplot as plt

# Data
percentages = [0.033204953, 0.035312768, 0.059338414, 0.024828139, 0.011421098, 
               0.082448244, 0.004938814, 0.034162189, 0.279342899, 0.069015662, 
               0.053189933, 0.079539803, 0.025417902, 0.117963582, 0.044018864, 0.045856735]
instructions = ['ADDIU', 'SW', 'BNE', 'SLL', 'BEQ', 'LW', 'SUBU', 'ADDU', 'MULT', 
                'MFLO', 'SLTU', 'LBU', 'MFHI', 'MULTU', 'DIV', 'Others']

# Function to only show percentage if it is larger than 5%
def autopct(pct):
    return ('%1.1f%%' % pct) if pct > 2 else ''

# Define colors
colors = plt.cm.tab20(range(len(instructions)))

# Explode the slices for visibility
explode = [0.05]*len(instructions)

# Create pie chart
fig, ax = plt.subplots()
wedges, text, autotexts = ax.pie(percentages, explode=explode, labels=instructions, 
                                 autopct=autopct, shadow=True, startangle=140, 
                                 colors=colors, pctdistance=0.85)

# Draw a white circle at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Add a legend
ax.legend(wedges, instructions, title="Instructions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Set the autopct colors
plt.setp(autotexts, size=8, color='white')

# Set the title of the plot
plt.title('Instruction Percentage', y=1.1)

plt.show()

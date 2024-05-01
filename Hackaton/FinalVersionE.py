
#student names and results need to be changed


import matplotlib.pyplot as plt
import numpy as np

Module = ("CS4222", "CS4221", "CS4141")
StudentLegend = {
    'Student1': (18, 18, 14),
    'Student2': (38, 48, 47),
    'Student3': (80, 35, 54),
    'Student4': (89, 26, 37),
    'Student5': (72, 63, 59),
}

x = np.arange(len(Module))  # the label locations
width = 0.15  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in StudentLegend.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Marks')
ax.set_title('Distribution of marks')
ax.set_xticks(x + width, Module)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 100)

plt.show()
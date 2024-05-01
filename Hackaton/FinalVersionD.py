
#student names and results need to be changed


import matplotlib.pyplot as plt
import numpy as np

Module = ("CS4222",)
OperationLegend = {
    'Sort': (18),
    'Search': (38),
}

x = np.arange(len(Module))  # the label locations
width = 0.1  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in OperationLegend.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time(ns)')
ax.set_xlabel('Operations')
ax.set_title('OperationsTime')
ax.set_xticks([])
ax.legend(loc='upper left', ncols=3)
ax.set_ylim()

plt.show()
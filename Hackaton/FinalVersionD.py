
#the timing needs to be changed to a variable of the main code


import matplotlib.pyplot as plt
import numpy as np

algorithms = ["Sort","Search"]
timing = [34,100]
width = [.6]

colors = ["green", "blue"]
plt.bar(algorithms, timing, color=colors, width = width)
plt.title("Time Complexity Graph", fontsize=14)
plt.xlabel("Operation", fontsize=14)
plt.ylabel("Time (ns)", fontsize=14)
plt.grid(False)
plt.show()

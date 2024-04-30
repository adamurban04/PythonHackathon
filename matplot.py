import matplotlib.pyplot as plt

algorithms = ["enda", "james", "andrei", "Adam"]
timing = [1, 100, 50, 10]

colors = ["green", "blue", "purple", "brown"]
plt.bar(algorithms, timing, color=colors)
plt.title("height levels", fontsize=14)
plt.xlabel("Subjects", fontsize=14)
plt.ylabel("Height", fontsize=14)
plt.grid(False)
plt.show()




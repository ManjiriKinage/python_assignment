import numpy as np
import matplotlib.pyplot as plt

# Create NumPy dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

# -------- Line Plot --------
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# -------- Bar Plot --------
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# -------- Scatter Plot --------
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# -------- Histogram --------
data = np.array([10, 20, 20, 30, 30, 30, 40, 50, 50])

plt.figure()
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

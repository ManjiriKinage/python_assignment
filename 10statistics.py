import pandas as pd

data = pd.read_csv("ages.csv")

ages = data["Age"]

print("Average Age:", ages.mean())
print("Mean Age:", ages.mean())
print("Median Age:", ages.median())
print("Highest Age:", ages.max())
print("Lowest Age:", ages.min())


# OR 

import pandas as pd
import statistics

data = pd.read_csv("ages.csv")

# Convert Age column to list
ages = data["Age"].tolist()

# Use statistics module
print("Ages:", ages)
print("Average Age:", statistics.mean(ages))
print("Mean Age:", statistics.mean(ages))
print("Median Age:", statistics.median(ages))
print("Highest Age:", max(ages))
print("Lowest Age:", min(ages))

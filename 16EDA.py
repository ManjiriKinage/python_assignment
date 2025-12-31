import pandas as pd
import numpy as np

# ---------- Create Sample Dataset ----------
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Amit"],
    "Age": [22, 25, np.nan, 23, 22],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Salary": [12000, 15000, 8000, None, 12000]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

# ---------- Data Cleaning ----------
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df.drop_duplicates(inplace=True)

# ---------- Data Preprocessing ----------
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

# ---------- Exploratory Data Analysis ----------
print("\nCleaned Dataset:\n", df)
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nGender Count:")
print(df["Gender"].value_counts())

print("\nAverage Salary:", df["Salary"].mean())

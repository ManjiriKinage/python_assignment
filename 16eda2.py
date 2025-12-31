import pandas as pd
import numpy as np

data={
    "Name" : ["Amit", "Neha", "Rahul", "Amit"],
     "Age": [22, 25, np.nan, 22],
    "Salary": [12000, 15000, 8000, 12000]
}
df= pd.DataFrame(data)
print("original data :\n " ,df)

#data cleaning
df["Age"]=df["Age"].fillna(df["Age"].mean())
df.drop_duplicates(inplace=True)

# 3. Data Preprocessing

df["Age"]=df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)

#EDA

print("\nCleaned Data:\n", df)
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

print("avg sal : ",df["Salary"].mean())


#EDA is the process of analyzing data to understand its structure, patterns, and summary statistics.
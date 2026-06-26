import pandas as pd

# Load Dataset
df = pd.read_csv("data/Dataset1.csv")

print("=" * 50)
print("TRAIN JOURNEY DATASET")
print("=" * 50)

# First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset Shape
print("\nRows and Columns")
print(df.shape)

# Column Names
print("\nColumn Names")
print(df.columns)

# Data Types
print("\nData Types")
print(df.dtypes)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated().sum())
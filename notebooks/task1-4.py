import pandas as pd

# Load Dataset
df = pd.read_csv("data/Dataset1.csv")

print("=" * 60)
print("TASK 1.4 - DATA QUALITY CHECK")
print("=" * 60)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# Negative Distance
negative_distance = df[df["Distance"] < 0]
print("\nNegative Distance Records:", len(negative_distance))

# Empty Station Name
empty_station = df[df["Station_Name"].astype(str).str.strip() == ""]
print("Empty Station Names:", len(empty_station))

# Empty Station Code
empty_code = df[df["Station_Code"].astype(str).str.strip() == ""]
print("Empty Station Codes:", len(empty_code))
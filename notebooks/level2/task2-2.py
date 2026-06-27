import pandas as pd

# Load Clean Dataset
df = pd.read_csv("data/Dataset1_Clean.csv")

print("=" * 60)
print("LEVEL 2 - TASK 2.2 : TIME CONVERSION")
print("=" * 60)

# Convert Time Columns
df["Arrival_time"] = pd.to_datetime(
    df["Arrival_time"],
    format="%H:%M:%S",
    errors="coerce"
)

df["Departure_Time"] = pd.to_datetime(
    df["Departure_Time"],
    format="%H:%M:%S",
    errors="coerce"
)

# Convert Time to Total Minutes
df["Arrival_Minutes"] = (
    df["Arrival_time"].dt.hour * 60
    + df["Arrival_time"].dt.minute
)

df["Departure_Minutes"] = (
    df["Departure_Time"].dt.hour * 60
    + df["Departure_Time"].dt.minute
)

print("\nConverted Time Columns:")
print(df[[
    "Arrival_time",
    "Departure_Time",
    "Arrival_Minutes",
    "Departure_Minutes"
]].head())

# Save Dataset
df.to_csv("data/Dataset2_Time.csv", index=False)

print("\n" + "=" * 60)
print("Task 2.2 Completed Successfully")
print("Dataset Saved as : Dataset2_Time.csv")
print("=" * 60)
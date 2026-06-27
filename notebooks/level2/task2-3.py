import pandas as pd

# Load Dataset
df = pd.read_csv("data/Dataset2_Time.csv")

print("=" * 60)
print("LEVEL 2 - TASK 2.3 : JOURNEY DURATION")
print("=" * 60)

# Calculate Journey Duration
df["Journey_Duration"] = df["Departure_Minutes"] - df["Arrival_Minutes"]

# Handle trains crossing midnight
df.loc[df["Journey_Duration"] < 0, "Journey_Duration"] += 1440

print("\nJourney Duration:")
print(df[[
    "Arrival_Minutes",
    "Departure_Minutes",
    "Journey_Duration"
]].head())

# Save Dataset
df.to_csv("data/Dataset3_Duration.csv", index=False)

print("\n" + "=" * 60)
print("Task 2.3 Completed Successfully")
print("Dataset Saved as : Dataset3_Duration.csv")
print("=" * 60)
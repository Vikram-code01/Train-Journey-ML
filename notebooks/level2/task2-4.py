import pandas as pd

# Load Dataset
df = pd.read_csv("data/Dataset3_Duration.csv")

print("=" * 60)
print("LEVEL 2 - TASK 2.4 : FEATURE ENGINEERING")
print("=" * 60)

# Total Distance for each Train
distance_table = df.groupby("Train_No")["Distance"].sum().reset_index()
distance_table.rename(columns={"Distance": "Total_Distance"}, inplace=True)

# Total Stops for each Train
stops_table = df.groupby("Train_No").size().reset_index(name="Total_Stops")

# Merge Features
df = df.merge(distance_table, on="Train_No", how="left")
df = df.merge(stops_table, on="Train_No", how="left")

print("\nNew Features Created Successfully\n")
print(df[[
    "Train_No",
    "Total_Distance",
    "Total_Stops",
    "Journey_Duration"
]].head())

# Save Dataset
df.to_csv("data/Dataset4_Features.csv", index=False)

print("\n" + "=" * 60)
print("Task 2.4 Completed Successfully")
print("Dataset Saved as : Dataset4_Features.csv")
print("=" * 60)
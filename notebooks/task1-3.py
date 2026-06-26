import pandas as pd

# Load Dataset
df = pd.read_csv("data/Dataset1.csv")

print("=" * 60)
print("TASK 1.3 - DISTANCE & STOPS STATISTICS")
print("=" * 60)

# Distance Statistics
print("\nDistance Statistics")
print(df["Distance"].describe())

# Number of Stops for each Train
stops = df.groupby("Train_No").size().reset_index(name="Total_Stops")

print("\nTrain-wise Number of Stops")
print(stops.head(20))

# Overall Statistics
print("\nTotal Trains :", stops.shape[0])
print("Average Stops :", round(stops["Total_Stops"].mean(), 2))
print("Maximum Stops :", stops["Total_Stops"].max())
print("Minimum Stops :", stops["Total_Stops"].min())
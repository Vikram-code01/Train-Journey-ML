import pandas as pd

# Load Dataset
df = pd.read_csv("data/Dataset1.csv")

# Train-wise Start and End Station
train_table = df.groupby("Train_No").agg(
    Starting_Station=("Station_Name", "first"),
    Ending_Station=("Station_Name", "last")
).reset_index()

print("=" * 60)
print("TASK 1.2 - TRAIN STARTING & ENDING STATIONS")
print("=" * 60)

print(train_table.head(20))
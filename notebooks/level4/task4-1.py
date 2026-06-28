import pandas as pd
from sklearn.model_selection import train_test_split

print("=" * 60)
print("LEVEL 4 - TASK 4.1 : TRAIN TEST SPLIT")
print("=" * 60)

# Load Dataset
df = pd.read_csv("data/Dataset4_Features.csv")

# Features and Target
X = df[["Total_Distance", "Total_Stops"]]
y = df["Journey_Duration"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

print("\nTask 4.1 Completed Successfully")

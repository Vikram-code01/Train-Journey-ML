import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

print("=" * 60)
print("LEVEL 5 - TASK 5.2 : RANDOM FOREST MODEL")
print("=" * 60)

# Load Dataset
df = pd.read_csv("data/Dataset4_Features.csv")

# Features and Target
X = df[["Total_Distance", "Total_Stops"]]
y = df["Journey_Duration"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

print("\nRandom Forest Model Trained Successfully")

print("\nTask 5.2 Completed Successfully")
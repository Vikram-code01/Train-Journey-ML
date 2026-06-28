import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

print("=" * 60)
print("LEVEL 6 - TASK 6.1 : SAVE TRAINED MODEL")
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

# Train Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "models/train_model.pkl")

print("\nModel saved successfully as models/train_model.pkl")
print("\nTask 6.1 Completed Successfully")
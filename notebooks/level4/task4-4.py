import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("=" * 60)
print("LEVEL 4 - TASK 4.4 : MODEL EVALUATION")
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

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("R2 Score :", r2_score(y_test, y_pred))

print("\nTask 4.4 Completed Successfully")
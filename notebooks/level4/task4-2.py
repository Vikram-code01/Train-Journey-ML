import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("=" * 60)
print("LEVEL 4 - TASK 4.2 : LINEAR REGRESSION MODEL")
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
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Trained Successfully")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

print("\nTask 4.2 Completed Successfully")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

print("=" * 60)
print("LEVEL 5 - TASK 5.3 : MODEL COMPARISON")
print("=" * 60)

# Load Dataset
df = pd.read_csv("data/Dataset4_Features.csv")

X = df[["Total_Distance", "Total_Stops"]]
y = df["Journey_Duration"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Decision Tree
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
dt_score = r2_score(y_test, dt.predict(X_test))

# Random Forest
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
rf_score = r2_score(y_test, rf.predict(X_test))

print("Decision Tree R2 Score :", dt_score)
print("Random Forest R2 Score :", rf_score)

print("\nTask 5.3 Completed Successfully")
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/Dataset4_Features.csv")

print("=" * 60)
print("LEVEL 3 - TASK 3.1 : DISTANCE VS JOURNEY DURATION")
print("=" * 60)

# Create Figure
plt.figure(figsize=(10, 6))

# Scatter Plot
plt.scatter(
    df["Total_Distance"],
    df["Journey_Duration"],
    alpha=0.5
)

# Title & Labels
plt.title("Distance vs Journey Duration")
plt.xlabel("Total Distance")
plt.ylabel("Journey Duration (Minutes)")

# Grid
plt.grid(True)

# Save Graph
plt.savefig("images/task3_1_distance_vs_duration.png")

# Show Graph
plt.show()

print("\nTask 3.1 Completed Successfully")
print("Graph Saved: images/task3_1_distance_vs_duration.png")
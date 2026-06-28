import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/Dataset4_Features.csv")

# Plot
plt.figure(figsize=(10,6))
plt.scatter(df["Total_Stops"], df["Journey_Duration"], alpha=0.6)

plt.title("Number of Stops vs Journey Duration")
plt.xlabel("Total Stops")
plt.ylabel("Journey Duration (Minutes)")
plt.grid(True)

# Save graph
plt.savefig("images/task3_2_stops_vs_duration.png")

# Show graph
plt.show()

print("=" * 60)
print("LEVEL 3 - TASK 3.2 : VISUALIZATION")
print("=" * 60)
print("Graph Created Successfully")
print("Graph saved as: images/task3_2_stops_vs_duration.png")
print("Task 3.2 Completed Successfully")
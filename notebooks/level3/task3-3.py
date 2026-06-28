import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 3 - TASK 3.3 : CORRELATION VISUALIZATION")
print("=" * 60)

# Load Dataset
df = pd.read_csv("data/Dataset4_Features.csv")

# Select Numeric Columns
numeric_df = df[["Total_Distance", "Total_Stops", "Journey_Duration"]]

# Correlation Matrix
corr = numeric_df.corr()

print("\nCorrelation Matrix:\n")
print(corr)

# Plot Heatmap
plt.figure(figsize=(6,5))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

# Write values inside cells
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}",
                 ha="center", va="center", color="black")

plt.tight_layout()

# Save graph
plt.savefig("images/task3_3_correlation.png")

# Show graph
plt.show()

print("\nTask 3.3 Completed Successfully")
print("Graph saved as: images/task3_3_correlation.png")
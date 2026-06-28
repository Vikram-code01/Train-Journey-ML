import pandas as pd

print("=" * 60)
print("LEVEL 3 - TASK 3.4 : PIVOT TABLE")
print("=" * 60)

# Load dataset
df = pd.read_csv("data/Dataset4_Features.csv")

# Create Pivot Table
pivot_table = pd.pivot_table(
    df,
    values="Total_Stops",
    index="Train_No",
    aggfunc="max"
)

print("\nPivot Table:\n")
print(pivot_table.head(10))

# Save Pivot Table
pivot_table.to_csv("data/Dataset5_PivotTable.csv")

print("\n" + "=" * 60)
print("Task 3.4 Completed Successfully")
print("Pivot Table saved as : Dataset5_PivotTable.csv")
print("=" * 60)
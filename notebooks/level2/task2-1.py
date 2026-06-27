# ==========================================================
# MACHINE LEARNING PROJECT
# Level 2 : Data Cleaning & Feature Engineering
# Task 2.1 : Handle Missing Values & Remove Duplicate Records
#
# Author : Vikram Kumar
# ==========================================================

# -------------------------
# Import Required Library
# -------------------------
import pandas as pd

# -------------------------
# Load Dataset
# -------------------------
df = pd.read_csv("data/Dataset1.csv")

# -------------------------
# Project Heading
# -------------------------
print("=" * 70)
print("LEVEL 2 - TASK 2.1 : DATA CLEANING")
print("=" * 70)

# -------------------------
# Dataset Shape Before Cleaning
# -------------------------
print("\nDataset Shape Before Cleaning:")
print(df.shape)

# -------------------------
# Check Missing Values
# -------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# -------------------------
# Fill Missing Values
# (Forward Fill)
# -------------------------
df = df.ffill()

# -------------------------
# Check Missing Values Again
# -------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -------------------------
# Check Duplicate Records
# -------------------------
duplicate_rows = df.duplicated().sum()

print("\nDuplicate Rows Found:")
print(duplicate_rows)

# -------------------------
# Remove Duplicate Records
# -------------------------
df = df.drop_duplicates()

# -------------------------
# Dataset Shape After Cleaning
# -------------------------
print("\nDataset Shape After Cleaning:")
print(df.shape)

# -------------------------
# Save Clean Dataset
# -------------------------
df.to_csv("data/Dataset1_Clean.csv", index=False)

# -------------------------
# Task Completed
# -------------------------
print("\n" + "=" * 70)
print("Task 2.1 Completed Successfully")
print("Clean Dataset Saved as : Dataset1_Clean.csv")
print("=" * 70)
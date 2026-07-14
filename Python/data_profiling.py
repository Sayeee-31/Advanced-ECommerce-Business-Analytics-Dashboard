import pandas as pd

# Load Dataset
orders = pd.read_csv("Data/raw/olist_orders_dataset.csv")

# First 5 Rows
print("First 5 Rows")
print(orders.head())

# Dataset Shape
print("\nDataset Shape")
print(orders.shape)

# Column Names
print("\nColumn Names")
print(orders.columns)

# Data Types
print("\nData Types")
print(orders.dtypes)

# Missing Values
print("\nMissing Values")
print(orders.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows")
print(orders.duplicated().sum())

# Order Status Count
print("\nOrder Status Count")
print(orders["order_status"].value_counts())

# Summary Statistics
print("\nSummary Statistics")
print(orders.describe(include="all"))
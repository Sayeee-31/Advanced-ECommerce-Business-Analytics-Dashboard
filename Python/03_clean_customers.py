import pandas as pd

# Load dataset
customers = pd.read_csv("Data/raw/olist_customers_dataset.csv")

# Remove duplicate rows
customers.drop_duplicates(inplace=True)

# Check missing values
print(customers.isnull().sum())

# Save cleaned dataset
customers.to_csv("Data/cleaned/olist_customers_cleaned.csv", index=False)

print("Customers dataset cleaned successfully.")
import pandas as pd

# Read orders dataset
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# Remove duplicate rows
orders = orders.drop_duplicates()

# Convert date columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# Save cleaned dataset
orders.to_csv("data/cleaned/olist_orders_cleaned.csv", index=False)

print("Orders dataset cleaned successfully!")
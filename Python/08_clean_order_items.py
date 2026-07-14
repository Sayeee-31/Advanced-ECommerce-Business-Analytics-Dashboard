import pandas as pd

items = pd.read_csv("Data/raw/olist_order_items_dataset.csv")

items.drop_duplicates(inplace=True)

print(items.isnull().sum())

items.to_csv("Data/cleaned/olist_order_items_cleaned.csv", index=False)

print("Order Items dataset cleaned successfully.")
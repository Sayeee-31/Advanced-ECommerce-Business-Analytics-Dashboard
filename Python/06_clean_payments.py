import pandas as pd

payments = pd.read_csv("Data/raw/olist_order_payments_dataset.csv")

payments.drop_duplicates(inplace=True)

print(payments.isnull().sum())

payments.to_csv("Data/cleaned/olist_order_payments_cleaned.csv", index=False)

print("Payments dataset cleaned successfully.")
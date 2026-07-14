import pandas as pd

sellers = pd.read_csv("Data/raw/olist_sellers_dataset.csv")

sellers.drop_duplicates(inplace=True)

print(sellers.isnull().sum())

sellers.to_csv("Data/cleaned/olist_sellers_cleaned.csv", index=False)

print("Sellers dataset cleaned successfully.")
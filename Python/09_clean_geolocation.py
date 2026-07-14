import pandas as pd

geo = pd.read_csv("Data/raw/olist_geolocation_dataset.csv")

geo.drop_duplicates(inplace=True)

print(geo.isnull().sum())

geo.to_csv("Data/cleaned/olist_geolocation_cleaned.csv", index=False)

print("Geolocation dataset cleaned successfully.")
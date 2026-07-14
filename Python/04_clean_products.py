import pandas as pd

# Load dataset
products = pd.read_csv("Data/raw/olist_products_dataset.csv")

# Remove duplicates
products.drop_duplicates(inplace=True)

# Fill missing values
products["product_category_name"] = products["product_category_name"].fillna("Unknown")
products["product_name_lenght"] = products["product_name_lenght"].fillna(0)
products["product_description_lenght"] = products["product_description_lenght"].fillna(0)
products["product_photos_qty"] = products["product_photos_qty"].fillna(0)

products["product_weight_g"] = products["product_weight_g"].fillna(products["product_weight_g"].median())
products["product_length_cm"] = products["product_length_cm"].fillna(products["product_length_cm"].median())
products["product_height_cm"] = products["product_height_cm"].fillna(products["product_height_cm"].median())
products["product_width_cm"] = products["product_width_cm"].fillna(products["product_width_cm"].median())

# Convert data types
products["product_name_lenght"] = products["product_name_lenght"].astype(int)
products["product_description_lenght"] = products["product_description_lenght"].astype(int)
products["product_photos_qty"] = products["product_photos_qty"].astype(int)

# Verify missing values
print(products.isnull().sum())

# Save cleaned dataset
products.to_csv("Data/cleaned/olist_products_cleaned.csv", index=False)

print("Products dataset cleaned successfully.")
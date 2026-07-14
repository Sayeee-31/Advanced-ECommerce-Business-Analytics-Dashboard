import pandas as pd

# Load dataset
reviews = pd.read_csv("Data/raw/olist_order_reviews_dataset.csv")

# Remove duplicates
reviews.drop_duplicates(inplace=True)

# Convert date columns
reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"])
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"])

# Fill missing text values
reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No Title")
reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No Comment")

# Check missing values
print(reviews.isnull().sum())

# Save cleaned dataset
reviews.to_csv("Data/cleaned/olist_order_reviews_cleaned.csv", index=False)

print("\nReviews dataset cleaned successfully.")
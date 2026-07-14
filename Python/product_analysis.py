import pandas as pd


def product_analysis(products):

    # Total Products
    total_products = products["product_id"].nunique()

    # Total Categories
    total_categories = (
        products["product_category_name"]
        .fillna("Unknown")
        .nunique()
    )

    # Top 10 Categories
    top_categories = (
        products["product_category_name"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_categories.columns = [
        "Category",
        "Products"
    ]

    result = {

        "Total Products": total_products,

        "Total Categories": total_categories,

        "Top Categories": top_categories

    }

    # Product Name Length
    if "product_name_lenght" in products.columns:

        result["Average Product Name Length"] = round(
            products["product_name_lenght"].mean(),
            2
        )

    elif "product_name_length" in products.columns:

        result["Average Product Name Length"] = round(
            products["product_name_length"].mean(),
            2
        )

    else:

        result["Average Product Name Length"] = "Column Not Available"

    # Product Description Length
    if "product_description_lenght" in products.columns:

        result["Average Description Length"] = round(
            products["product_description_lenght"].mean(),
            2
        )

    elif "product_description_length" in products.columns:

        result["Average Description Length"] = round(
            products["product_description_length"].mean(),
            2
        )

    else:

        result["Average Description Length"] = "Column Not Available"

    return result
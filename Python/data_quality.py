import pandas as pd


def data_quality(customers, orders, payments, products, sellers, order_items):

    datasets = {
        "Customers": customers,
        "Orders": orders,
        "Payments": payments,
        "Products": products,
        "Sellers": sellers,
        "Order Items": order_items
    }

    quality_report = []

    for name, df in datasets.items():

        total_rows = len(df)

        total_missing = df.isnull().sum().sum()

        duplicate_rows = df.duplicated().sum()

        total_cells = df.shape[0] * df.shape[1]

        completeness = (
            (total_cells - total_missing)
            / total_cells
        ) * 100

        quality_report.append({

            "Dataset": name,

            "Rows": total_rows,

            "Missing Values": int(total_missing),

            "Duplicate Rows": int(duplicate_rows),

            "Completeness (%)": round(completeness, 2)

        })

    quality_report = pd.DataFrame(quality_report)

    overall_score = round(
        quality_report["Completeness (%)"].mean(),
        2
    )

    return quality_report, overall_score
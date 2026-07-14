import pandas as pd


def outlier_analysis(payments):

    # Copy Data
    df = payments.copy()

    # Remove Missing Values
    df = df.dropna(subset=["payment_value"])

    # Calculate Quartiles
    q1 = df["payment_value"].quantile(0.25)
    q3 = df["payment_value"].quantile(0.75)

    # Interquartile Range
    iqr = q3 - q1

    # Lower & Upper Limits
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    # Detect Outliers
    outliers = df[
        (df["payment_value"] < lower) |
        (df["payment_value"] > upper)
    ]

    # Percentage
    percentage = (
        len(outliers) /
        len(df)
    ) * 100

    return {

        "Total Transactions":
            len(df),

        "Outlier Transactions":
            len(outliers),

        "Outlier Percentage (%)":
            round(percentage, 2),

        "Highest Payment":
            round(df["payment_value"].max(), 2),

        "Average Payment":
            round(df["payment_value"].mean(), 2),

        "Top 10 Outliers":
            outliers.sort_values(
                "payment_value",
                ascending=False
            ).head(10)

    }
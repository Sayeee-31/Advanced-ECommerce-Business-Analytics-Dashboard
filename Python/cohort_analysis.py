import pandas as pd


def cohort_analysis(orders):

    df = orders.copy()

    # Convert date column
    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"]
    )

    # Keep only completed orders
    df = df[
        df["order_status"] == "delivered"
    ]

    # Customer first purchase date
    df["customer_first_purchase"] = (
        df
        .groupby("customer_id")
        ["order_purchase_timestamp"]
        .transform("min")
    )

    # Create month columns

    df["order_month"] = (
        df["order_purchase_timestamp"]
        .dt
        .to_period("M")
    )

    df["cohort_month"] = (
        df["customer_first_purchase"]
        .dt
        .to_period("M")
    )


    # Calculate retention table

    cohort = (
        df
        .groupby(
            [
                "cohort_month",
                "order_month"
            ]
        )
        ["customer_id"]
        .nunique()
        .reset_index()
    )


    cohort.columns = [
        "Cohort Month",
        "Order Month",
        "Customers"
    ]


    # Calculate retention percentage

    cohort["Retention (%)"] = (
        cohort["Customers"] /
        cohort
        .groupby("Cohort Month")
        ["Customers"]
        .transform("first")
        *
        100
    )


    cohort["Retention (%)"] = (
        cohort["Retention (%)"]
        .round(2)
    )


    return cohort
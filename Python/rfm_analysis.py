import pandas as pd


def rfm_analysis(customers, orders, payments):

    # Merge all tables
    df = (
        customers
        .merge(
            orders,
            on="customer_id"
        )
        .merge(
            payments,
            on="order_id"
        )
    )

    # Convert to datetime
    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"]
    )

    # Latest purchase date
    snapshot_date = (
        df["order_purchase_timestamp"].max()
        + pd.Timedelta(days=1)
    )

    # -------------------------
    # RFM Metrics
    # -------------------------

    rfm = (
        df.groupby("customer_unique_id")
        .agg(
            Recency=(
                "order_purchase_timestamp",
                lambda x: (snapshot_date - x.max()).days
            ),
            Frequency=(
                "order_id",
                "nunique"
            ),
            Monetary=(
                "payment_value",
                "sum"
            )
        )
        .reset_index()
    )

    # -------------------------
    # Scores
    # -------------------------

    rfm["R_Score"] = pd.qcut(
        rfm["Recency"],
        5,
        labels=[5,4,3,2,1]
    )

    rfm["F_Score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        5,
        labels=[1,2,3,4,5]
    )

    rfm["M_Score"] = pd.qcut(
        rfm["Monetary"],
        5,
        labels=[1,2,3,4,5]
    )

    # -------------------------
    # Total Score
    # -------------------------

    rfm["RFM Score"] = (
        rfm["R_Score"].astype(str)
        + rfm["F_Score"].astype(str)
        + rfm["M_Score"].astype(str)
    )

    # -------------------------
    # Customer Segment
    # -------------------------

    def segment(row):

        if row["R_Score"] >= 4 and row["F_Score"] >= 4:
            return "Champions"

        elif row["R_Score"] >= 3 and row["F_Score"] >= 3:
            return "Loyal Customers"

        elif row["R_Score"] >= 4:
            return "Potential Loyalists"

        elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
            return "At Risk"

        else:
            return "Others"

    rfm["Segment"] = rfm.apply(segment, axis=1)

    segment_summary = (
        rfm["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_summary.columns = [
        "Customer Segment",
        "Customers"
    ]

    return rfm, segment_summary
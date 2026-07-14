import pandas as pd


def seller_analysis(order_items):

    # Seller Summary
    seller_summary = (
        order_items
        .groupby("seller_id")
        .agg(
            Orders=("order_id", "count"),
            Revenue=("price", "sum")
        )
        .sort_values("Revenue", ascending=False)
    )

    # Top Seller
    top_seller = seller_summary.iloc[0]

    # Total Revenue
    total_revenue = seller_summary["Revenue"].sum()

    # Contribution of Top Seller
    contribution = (
        top_seller["Revenue"] /
        total_revenue
    ) * 100

    # Total Sellers
    total_sellers = seller_summary.shape[0]

    # Average Revenue per Seller
    avg_revenue = (
        seller_summary["Revenue"].mean()
    )

    # Average Orders per Seller
    avg_orders = (
        seller_summary["Orders"].mean()
    )

    # Top 5 Sellers
    top5 = (
        seller_summary
        .head(5)
        .reset_index()
    )

    top5.columns = [
        "Seller ID",
        "Orders",
        "Revenue"
    ]

    return {

        "Total Sellers":
            total_sellers,

        "Top Seller":
            seller_summary.index[0],

        "Top Seller Revenue":
            round(top_seller["Revenue"], 2),

        "Top Seller Orders":
            int(top_seller["Orders"]),

        "Top Seller Contribution (%)":
            round(contribution, 2),

        "Average Revenue per Seller":
            round(avg_revenue, 2),

        "Average Orders per Seller":
            round(avg_orders, 2),

        "Top 5 Sellers":
            top5

    }
import pandas as pd


def delivery_analysis(orders):

    # Create a copy
    delivery_df = orders.copy()

    # Convert date columns
    delivery_df["order_purchase_timestamp"] = pd.to_datetime(
        delivery_df["order_purchase_timestamp"]
    )

    delivery_df["order_delivered_customer_date"] = pd.to_datetime(
        delivery_df["order_delivered_customer_date"]
    )

    delivery_df["order_estimated_delivery_date"] = pd.to_datetime(
        delivery_df["order_estimated_delivery_date"]
    )

    # Keep only delivered orders
    delivery_df = delivery_df[
        delivery_df["order_status"] == "delivered"
    ]

    # Remove rows with missing delivery dates
    delivery_df = delivery_df.dropna(
        subset=[
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    )

    # Delivery time
    delivery_df["delivery_days"] = (
        delivery_df["order_delivered_customer_date"]
        -
        delivery_df["order_purchase_timestamp"]
    ).dt.days

    average_days = delivery_df["delivery_days"].mean()
    fastest = delivery_df["delivery_days"].min()
    slowest = delivery_df["delivery_days"].max()

    # Delayed deliveries
    delayed = delivery_df[
        delivery_df["order_delivered_customer_date"] >
        delivery_df["order_estimated_delivery_date"]
    ]

    delayed_percent = (
        len(delayed) / len(delivery_df)
    ) * 100

    on_time_percent = 100 - delayed_percent

    return {

        "Average Delivery Days": round(average_days, 2),

        "Fastest Delivery": fastest,

        "Slowest Delivery": slowest,

        "Delayed Orders (%)": round(delayed_percent, 2),

        "On-Time Delivery (%)": round(on_time_percent, 2)

    }
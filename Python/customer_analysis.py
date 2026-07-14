import pandas as pd

def customer_analysis(customers, orders):

    # Merge orders with customers
    customer_data = orders.merge(
        customers,
        on="customer_id",
        how="inner"
    )

    customer_orders = (
        customer_data
        .groupby("customer_unique_id")
        .size()
    )

    total_customers = customer_data["customer_unique_id"].nunique()

    repeat_customers = (customer_orders > 1).sum()

    one_time_customers = (customer_orders == 1).sum()

    repeat_rate = (repeat_customers / total_customers) * 100

    avg_orders = customer_orders.mean()

    return {

        "Total Customers": total_customers,
        "Repeat Customers": repeat_customers,
        "One-Time Customers": one_time_customers,
        "Repeat Purchase Rate (%)": round(repeat_rate,2),
        "Average Orders per Customer": round(avg_orders,2)

    }
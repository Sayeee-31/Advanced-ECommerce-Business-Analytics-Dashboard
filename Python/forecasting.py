import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def revenue_forecast(orders, payments):

    # Merge tables
    revenue = orders.merge(
        payments,
        on="order_id"
    )

    # Convert to datetime
    revenue["order_purchase_timestamp"] = pd.to_datetime(
        revenue["order_purchase_timestamp"]
    )

    # Create Month column
    revenue["Month"] = (
        revenue["order_purchase_timestamp"]
        .dt.to_period("M")
    )

    # Monthly Revenue
    monthly = (
        revenue.groupby("Month")
        .agg(
            Revenue=("payment_value", "sum"),
            Orders=("order_id", "count")
        )
        .reset_index()
    )

    # Remove incomplete months
    monthly = monthly[
        monthly["Orders"] >= 500
    ].copy()

    monthly["Month"] = range(1, len(monthly) + 1)

    X = monthly[["Month"]]
    y = monthly["Revenue"]

    # Machine Learning Model
    model = LinearRegression()

    model.fit(X, y)

   # Predict next month (using DataFrame to avoid sklearn warning)
    next_month = pd.DataFrame({
    "Month": [len(monthly) + 1]
    })

    prediction = model.predict(next_month)[0]

    current = monthly.iloc[-1]["Revenue"]

    growth = (
    (prediction - current)
    / current
    * 100
    )
    return {

        "Current Month Revenue":
            round(current, 2),

        "Predicted Next Month":
            round(prediction, 2),

        "Predicted Growth (%)":
            round(growth, 2)

    }
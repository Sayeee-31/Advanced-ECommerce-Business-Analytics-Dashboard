import pandas as pd


def risk_analysis(orders):

    cancelled = (
        orders["order_status"]
        .eq("canceled")
        .sum()
    )

    unavailable = (
        orders["order_status"]
        .eq("unavailable")
        .sum()
    )

    total = len(orders)

    risk = ((cancelled + unavailable) / total) * 100

    return {
        "Cancelled Orders": cancelled,
        "Unavailable Orders": unavailable,
        "Business Risk (%)": round(risk,2)
    }
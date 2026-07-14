import pandas as pd


def payment_analysis(payments):

    total_revenue = round(
        payments["payment_value"].sum(),
        2
    )

    average_payment = round(
        payments["payment_value"].mean(),
        2
    )

    highest_payment = round(
        payments["payment_value"].max(),
        2
    )

    lowest_payment = round(
        payments["payment_value"].min(),
        2
    )

    average_installments = round(
        payments["payment_installments"].mean(),
        2
    )

    payment_distribution = (
        payments["payment_type"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    payment_distribution.columns = [
        "Payment Type",
        "Percentage (%)"
    ]

    most_used = (
        payments["payment_type"]
        .mode()[0]
    )

    return {

        "Total Revenue": total_revenue,

        "Average Payment": average_payment,

        "Highest Payment": highest_payment,

        "Lowest Payment": lowest_payment,

        "Average Installments": average_installments,

        "Most Used Payment": most_used,

        "Payment Distribution": payment_distribution

    }
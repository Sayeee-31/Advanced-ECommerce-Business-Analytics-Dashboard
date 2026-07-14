import matplotlib.pyplot as plt


def revenue_chart(payments):

    payment = (
        payments
        .groupby("payment_type")["payment_value"]
        .sum()
    )

    plt.figure(figsize=(8,5))

    payment.plot(kind="bar")

    plt.title("Revenue by Payment Type")

    plt.xlabel("Payment Type")

    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.savefig("../reports/payment_revenue.png")

    plt.close()
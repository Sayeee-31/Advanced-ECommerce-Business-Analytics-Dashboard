def generate_business_insights(
    kpis,
    customer,
    seller,
    product,
    payment,
    risk,
    forecast
):

    insights = []

    # -----------------------------
    # Revenue Insight
    # -----------------------------
    revenue = kpis["Total Revenue"]

    if revenue >= 15000000:
        insights.append(
            f"Revenue has crossed ₹{revenue:,.0f}, indicating excellent business performance."
        )
    else:
        insights.append(
            "Revenue is below the desired target."
        )

    # -----------------------------
    # Customer Insight
    # -----------------------------
    repeat_rate = customer["Repeat Purchase Rate (%)"]

    if repeat_rate < 10:
        insights.append(
            f"Only {repeat_rate:.2f}% customers made repeat purchases. Introduce loyalty programs to improve retention."
        )
    else:
        insights.append(
            f"Repeat purchase rate is healthy at {repeat_rate:.2f}%."
        )

    # -----------------------------
    # Payment Insight
    # -----------------------------
    payment_type = payment["Most Used Payment"]

    insights.append(
        f"The most preferred payment method is '{payment_type}'. Promotions can focus on this payment option."
    )

    # -----------------------------
    # Seller Insight
    # -----------------------------
    contribution = seller["Top Seller Contribution (%)"]

    if contribution < 5:
        insights.append(
            f"The top seller contributes only {contribution:.2f}% of revenue, indicating a healthy distribution across sellers."
        )
    else:
        insights.append(
            f"The top seller contributes {contribution:.2f}% of revenue. Consider reducing dependency on a few sellers."
        )

    # -----------------------------
    # Product Insight
    # -----------------------------
    top_category = product["Top Categories"].iloc[0]["Category"]

    insights.append(
        f"'{top_category}' is the leading product category by catalog size."
    )

    # -----------------------------
    # Risk Insight
    # -----------------------------
    business_risk = risk["Business Risk (%)"]

    if business_risk < 2:
        insights.append(
            f"Business risk is low ({business_risk:.2f}%), indicating stable operations."
        )
    else:
        insights.append(
            f"Business risk is {business_risk:.2f}%. Focus on reducing cancelled and unavailable orders."
        )

    # -----------------------------
    # Forecast Insight
    # -----------------------------
    growth = forecast["Predicted Growth (%)"]

    if growth > 0:
        insights.append(
            f"Machine Learning predicts a revenue growth of {growth:.2f}% next month."
        )
    else:
        insights.append(
            f"Machine Learning predicts a revenue decline of {abs(growth):.2f}% next month."
        )

    return insights
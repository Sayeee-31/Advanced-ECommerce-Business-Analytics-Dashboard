def executive_dashboard(
    kpis,
    score,
    status,
    customer,
    seller,
    payment,
    risk,
    forecast
):

    print("\n")
    print("=" * 70)
    print("                 BUSINESS MRI EXECUTIVE DASHBOARD")
    print("=" * 70)

    print(f"Business Health Score        : {score}/100")
    print(f"Business Status              : {status}")

    print("-" * 70)

    print(f"Revenue                      : ₹{kpis['Total Revenue']:,.2f}")
    print(f"Average Order Value          : ₹{kpis['Average Order Value']:.2f}")
    print(f"Customers                    : {kpis['Total Customers']:,}")
    print(f"Orders                       : {kpis['Total Orders']:,}")

    print("-" * 70)

    print(f"Repeat Purchase Rate         : {customer['Repeat Purchase Rate (%)']:.2f}%")
    print(f"Top Seller Contribution      : {seller['Top Seller Contribution (%)']:.2f}%")
    print(f"Preferred Payment            : {payment['Most Used Payment']}")
    print(f"Business Risk                : {risk['Business Risk (%)']:.2f}%")

    print("-" * 70)

    print(f"Forecast Growth              : {forecast['Predicted Growth (%)']:.2f}%")
    print(f"Predicted Revenue            : ₹{forecast['Predicted Next Month']:,.2f}")

    print("=" * 70)
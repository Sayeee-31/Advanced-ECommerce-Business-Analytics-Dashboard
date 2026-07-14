def calculate_score(kpis):

    revenue = kpis["Total Revenue"]

    customers = kpis["Total Customers"]

    sellers = kpis["Total Sellers"]

    products = kpis["Total Products"]

    aov = kpis["Average Order Value"]

    # Revenue (30)

    revenue_score = min(
        30,
        (revenue / 16000000) * 30
    )

    # Customer (20)

    customer_score = min(
        20,
        (customers / 100000) * 20
    )

    # Seller (15)

    seller_score = min(
        15,
        (sellers / 3500) * 15
    )

    # Product (15)

    product_score = min(
        15,
        (products / 35000) * 15
    )

    # Average Order Value (20)

    aov_score = min(
        20,
        (aov / 200) * 20
    )

    total_score = round(

        revenue_score +

        customer_score +

        seller_score +

        product_score +

        aov_score

    )

    if total_score >= 90:

        status = "Excellent"

    elif total_score >= 75:

        status = "Healthy"

    elif total_score >= 60:

        status = "Average"

    else:

        status = "Critical"

    return total_score, status
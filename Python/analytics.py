def calculate_kpis(customers, orders, payments, products, sellers):

    total_revenue = payments["payment_value"].sum()
    average_order_value = payments["payment_value"].mean()
    total_customers = customers["customer_id"].nunique()
    total_orders = orders["order_id"].nunique()
    total_products = products["product_id"].nunique()
    total_sellers = sellers["seller_id"].nunique()

    kpis = {

        "Total Revenue": total_revenue,
        "Average Order Value": average_order_value,
        "Total Customers": total_customers,
        "Total Orders": total_orders,
        "Total Products": total_products,
        "Total Sellers": total_sellers

    }

    return kpis
from database import connect_database
from database import load_tables

from analytics import calculate_kpis
from scoring import calculate_score
from recommendations import generate_recommendations
from report import print_report
from delivery import delivery_analysis

from customer_analysis import customer_analysis
from seller_analysis import seller_analysis
from product_analysis import product_analysis
from payment_analysis import payment_analysis
from risk_analysis import risk_analysis
from forecasting import revenue_forecast
from visualization import revenue_chart
from rfm_analysis import rfm_analysis
from business_insights import generate_business_insights
from executive_dashboard import executive_dashboard
from data_quality import data_quality
from outlier_analysis import outlier_analysis
from cohort_analysis import cohort_analysis
from profitability_analysis import profitability_analysis
from powerbi_export import export_powerbi_data

def main():

    print("=" * 50)
    print("        BUSINESS MRI ANALYTICS SYSTEM")
    print("=" * 50)

    # Connect Database
    conn = connect_database()

    # Load Tables
    customers, orders, payments, products, sellers, order_items = load_tables(conn)


    # KPI Analysis
    kpis = calculate_kpis(
        customers,
        orders,
        payments,
        products,
        sellers
    )

    # Business Score
    score, status = calculate_score(kpis)

    # Recommendations
    recommendations = generate_recommendations(kpis)

    # Delivery Analytics
    delivery = delivery_analysis(orders)

    # Customer Analytics
    customer = customer_analysis(customers, orders)

    # Seller Analytics
    seller = seller_analysis(order_items)
    print(seller.keys())

    # Product Analytics
    product = product_analysis(products)

    # Payment Analytics
    payment = payment_analysis(payments)

    # Risk Analysis
    risk = risk_analysis(orders)

    # Profitability Analysis
    profitability = profitability_analysis(
    order_items,
    orders
    )


    quality_report, quality_score = data_quality(
    customers,
    orders,
    payments,
    products,
    sellers,
    order_items
    )

    outliers = outlier_analysis(payments)

    # Revenue Forecast
    forecast = revenue_forecast(orders, payments)


    rfm, segment_summary = rfm_analysis(
    customers,
    orders,
    payments
    )


    cohort = cohort_analysis(
    orders
    )
    

    insights = generate_business_insights(
    kpis,
    customer,
    seller,
    product,
    payment,
    risk,
    forecast
    )

    executive_dashboard(
    kpis,
    score,
    status,
    customer,
    seller,
    payment,
    risk,
    forecast
    )

    # Print Business Report
    print_report(
        kpis,
        score,
        status,
        recommendations
    )

    # Delivery Analytics
    print("\n" + "=" * 60)
    print("DELIVERY ANALYTICS")
    print("=" * 60)

    for key, value in delivery.items():
        print(f"{key:<35}: {value}")

    # Customer Analytics
    print("\n" + "=" * 60)
    print("CUSTOMER ANALYTICS")
    print("=" * 60)

    for key, value in customer.items():
        print(f"{key:<35}: {value}")

   # Seller Analytics
    print("\n" + "=" * 60)
    print("SELLER ANALYTICS")
    print("=" * 60)

    for key, value in seller.items():

        if key == "Top 5 Sellers":
            print("\nTop 5 Sellers")
            print(value.to_string(index=False))
        else:
            print(f"{key:<35}: {value}")


    # Product Analytics
    print("\n" + "=" * 60)
    print("PRODUCT ANALYTICS")
    print("=" * 60)

    for key, value in product.items():

        if key == "Top Categories":
            print("\nTop Categories")
            print(value.to_string(index=False))
        else:
            print(f"{key:<35}: {value}")

    # Payment Analytics
    print("\n" + "=" * 60)
    print("PAYMENT ANALYTICS")
    print("=" * 60)

    for key, value in payment.items():

        if key == "Payment Distribution":
            print("\nPayment Distribution")
            print(value.to_string(index=False))
        else:
            print(f"{key:<35}: {value}")

   # PROFITABILITY ANALYSIS
    print("\n" + "=" * 60)
    print("PROFITABILITY ANALYSIS")
    print("=" * 60)

    for key, value in profitability.items():
        print(f"{key:<35}: {value}")


    # Risk Analysis
    print("\n" + "=" * 60)
    print("BUSINESS RISK")
    print("=" * 60)

    for key, value in risk.items():
        print(f"{key:<35}: {value}")

    
    # Data Quality
    print("\n" + "=" * 60)
    print("DATA QUALITY")
    print("=" * 60)

    print(quality_report.to_string(index=False))

    print(f"\nOverall Data Quality Score : {quality_score}%")
    

    #Outlier Analysis
    print("\n" + "=" * 60)
    print("OUTLIER ANALYSIS")
    print("=" * 60)

    for key, value in outliers.items():

        if key == "Top 10 Outliers":
            print("\nTop 10 Highest Payments")
            print(value.to_string(index=False))
        else:
            print(f"{key:<35}: {value}")
    
    # -------------------------
    # Revenue Forecast
    # -------------------------

    print("\n" + "=" * 60)
    print("REVENUE FORECAST")
    print("=" * 60)

    for key, value in forecast.items():

        if isinstance(value, float):
            print(f"{key:<35}: {value:,.2f}")
        else:
            print(f"{key:<35}: {value}")

    # -------------------------
    # RFM Customer Segmentation
    # -------------------------

    print("\n" + "=" * 60)
    print("RFM CUSTOMER SEGMENTATION")
    print("=" * 60)

    print(segment_summary.to_string(index=False))


    #CUSTOMER COHORT ANALYSIS
    print("\n" + "=" * 60)
    print("CUSTOMER COHORT ANALYSIS")
    print("=" * 60)

    print(
        cohort.head(20)
        .to_string(index=False)
    )

    # -------------------------
    # Business Insights
    # -------------------------

    print("\n" + "=" * 60)
    print("BUSINESS INSIGHTS")
    print("=" * 60)

    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")

   
    # -------------------------
    # Revenue Chart
    # -------------------------

    revenue_chart(payments)

    print("\n✅ Revenue Chart Generated Successfully!")
    print("📁 Check the reports folder.")


    # -------------------------
    # Power BI Export
    # -------------------------

    export_powerbi_data(
    kpis,
    customer,
    seller,
    product,
    payment,
    risk,
    forecast,
    segment_summary,
    quality_report,
    profitability,
    cohort
    )

    # -------------------------
    # Close Connection
    # -------------------------

    conn.dispose()      # or conn.close() if connect_database() returns a Connection

    print("\n" + "=" * 50)
    print("BUSINESS MRI COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()
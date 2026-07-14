import os
import pandas as pd


def export_powerbi_data(
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
):

    # Project root
    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    folder = os.path.join(
        project_root,
        "powerbi"
    )

    os.makedirs(folder, exist_ok=True)


    # -----------------------------
    # KPI Data
    # -----------------------------

    pd.DataFrame(
        list(kpis.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "kpis.csv"),
        index=False
    )


    # -----------------------------
    # Customer Analytics
    # -----------------------------

    pd.DataFrame(
        list(customer.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "customer_analysis.csv"),
        index=False
    )


    # -----------------------------
    # Seller Analytics
    # -----------------------------

    seller_basic = {
        key: value
        for key, value in seller.items()
        if key != "Top 5 Sellers"
    }

    pd.DataFrame(
        list(seller_basic.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "seller_analysis.csv"),
        index=False
    )


    # Top Sellers Table
    seller["Top 5 Sellers"].to_csv(
        os.path.join(folder, "top_sellers.csv"),
        index=False
    )


    # -----------------------------
    # Product Analytics
    # -----------------------------

    product["Top Categories"].to_csv(
        os.path.join(folder, "top_categories.csv"),
        index=False
    )


    # -----------------------------
    # Payment Analytics
    # -----------------------------

    payment_basic = {
        key: value
        for key, value in payment.items()
        if key != "Payment Distribution"
    }

    pd.DataFrame(
        list(payment_basic.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "payment_analysis.csv"),
        index=False
    )


    payment["Payment Distribution"].to_csv(
        os.path.join(folder, "payment_distribution.csv"),
        index=False
    )


    # -----------------------------
    # Business Risk
    # -----------------------------

    pd.DataFrame(
        list(risk.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "business_risk.csv"),
        index=False
    )


    # -----------------------------
    # Revenue Forecast
    # -----------------------------

    pd.DataFrame(
        list(forecast.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "revenue_forecast.csv"),
        index=False
    )


    # -----------------------------
    # RFM Segmentation
    # -----------------------------

    segment_summary.to_csv(
        os.path.join(folder, "rfm_segments.csv"),
        index=False
    )


    # -----------------------------
    # Data Quality
    # -----------------------------

    quality_report.to_csv(
        os.path.join(folder, "data_quality.csv"),
        index=False
    )


    # -----------------------------
    # Profitability
    # -----------------------------

    pd.DataFrame(
        list(profitability.items()),
        columns=[
            "Metric",
            "Value"
        ]
    ).to_csv(
        os.path.join(folder, "profitability.csv"),
        index=False
    )


    # -----------------------------
    # Cohort Analysis
    # -----------------------------

    cohort.to_csv(
        os.path.join(folder, "customer_cohort.csv"),
        index=False
    )


    print("\nPower BI Data Export Completed!")
    print(folder)
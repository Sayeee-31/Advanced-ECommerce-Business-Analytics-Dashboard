import pandas as pd


def profitability_analysis(order_items, orders):

    # Copy Data
    items = order_items.copy()


    # Calculate Revenue

    total_revenue = (
        items["price"]
        .sum()
    )


    # Estimated Cost
    # Assume 70% of selling price is cost

    estimated_cost = (
        total_revenue * 0.70
    )


    # Profit

    gross_profit = (
        total_revenue -
        estimated_cost
    )


    # Profit Margin

    profit_margin = (
        gross_profit /
        total_revenue
    ) * 100


    # Average Profit per Order

    total_orders = (
        orders["order_id"]
        .nunique()
    )


    avg_profit_order = (
        gross_profit /
        total_orders
    )


    return {

        "Total Revenue":
            round(total_revenue,2),

        "Estimated Cost":
            round(estimated_cost,2),

        "Gross Profit":
            round(gross_profit,2),

        "Profit Margin (%)":
            round(profit_margin,2),

        "Average Profit per Order":
            round(avg_profit_order,2)

    }
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="BussinessMRI",
    user="postgres",
    password="admin123",
    port="5432"
)

print("Connected Successfully")

customers = pd.read_sql("SELECT * FROM customers;", conn)
orders = pd.read_sql("SELECT * FROM orders;", conn)
payments = pd.read_sql("SELECT * FROM payments;", conn)
products = pd.read_sql("SELECT * FROM products;", conn)
sellers = pd.read_sql("SELECT * FROM sellers;", conn)
order_items = pd.read_sql("SELECT * FROM order_items;", conn)

print("Customers:", len(customers))
print("Orders:", len(orders))
print("Payments:", len(payments))
print("Products:", len(products))
print("Sellers:", len(sellers))
print("Order Items:", len(order_items))

conn.close()

# -----------------------------
# BUSINESS KPIs
# -----------------------------

total_revenue = payments["payment_value"].sum()
average_order_value = payments["payment_value"].mean()
total_customers = customers["customer_id"].nunique()
total_orders = orders["order_id"].nunique()
total_products = products["product_id"].nunique()
total_sellers = sellers["seller_id"].nunique()

print("\n========== BUSINESS KPIs ==========")
print(f"Total Revenue        : {total_revenue:.2f}")
print(f"Average Order Value  : {average_order_value:.2f}")
print(f"Total Customers      : {total_customers}")
print(f"Total Orders         : {total_orders}")
print(f"Total Products       : {total_products}")
print(f"Total Sellers        : {total_sellers}")


print("\n" + "="*60)
print("           BUSINESS MRI HEALTH SCORE")
print("="*60)

# ----------------------------
# Revenue Score (30 Marks)
# ----------------------------

if total_revenue >= 15000000:
    revenue_score = 30
elif total_revenue >= 10000000:
    revenue_score = 25
elif total_revenue >= 5000000:
    revenue_score = 18
else:
    revenue_score = 10

# ----------------------------
# Average Order Value (20 Marks)
# ----------------------------

if average_order_value >= 150:
    aov_score = 20
elif average_order_value >= 120:
    aov_score = 16
elif average_order_value >= 100:
    aov_score = 12
else:
    aov_score = 5

# ----------------------------
# Customer Base (20 Marks)
# ----------------------------

if total_customers >= 90000:
    customer_score = 20
elif total_customers >= 70000:
    customer_score = 15
elif total_customers >= 50000:
    customer_score = 10
else:
    customer_score = 5

# ----------------------------
# Seller Network (15 Marks)
# ----------------------------

if total_sellers >= 3000:
    seller_score = 15
elif total_sellers >= 2000:
    seller_score = 12
else:
    seller_score = 6

# ----------------------------
# Product Catalog (15 Marks)
# ----------------------------

if total_products >= 30000:
    product_score = 15
elif total_products >= 20000:
    product_score = 12
else:
    product_score = 6

# ----------------------------
# Overall Score
# ----------------------------

business_score = (
    revenue_score +
    aov_score +
    customer_score +
    seller_score +
    product_score
)

print(f"Revenue Score          : {revenue_score}/30")
print(f"AOV Score              : {aov_score}/20")
print(f"Customer Score         : {customer_score}/20")
print(f"Seller Score           : {seller_score}/15")
print(f"Product Score          : {product_score}/15")

print("-"*60)

print(f"Overall Business Score : {business_score}/100")

if business_score >= 90:
    status = "Excellent"
elif business_score >= 75:
    status = "Healthy"
elif business_score >= 60:
    status = "Average"
else:
    status = "Critical"

print(f"Business Status        : {status}")



print("\n" + "="*60)
print("          ROOT CAUSE ANALYSIS")
print("="*60)

issues = []

if revenue_score < 25:
    issues.append("Revenue is below target.")

if aov_score < 15:
    issues.append("Average Order Value is low.")

if seller_score < 10:
    issues.append("Seller network needs expansion.")

if product_score < 10:
    issues.append("Limited product catalog.")

if customer_score < 15:
    issues.append("Customer base needs growth.")

if len(issues) == 0:
    print("No major business issues detected.")
else:
    for i, issue in enumerate(issues, start=1):
        print(f"{i}. {issue}")



print("\n" + "="*60)
print("      BUSINESS RECOMMENDATIONS")
print("="*60)

recommendations = []

if revenue_score < 25:
    recommendations.append("Increase marketing campaigns.")

if aov_score < 15:
    recommendations.append("Launch combo offers and upselling.")

if seller_score < 10:
    recommendations.append("Onboard more sellers.")

if product_score < 10:
    recommendations.append("Expand product categories.")

if customer_score < 15:
    recommendations.append("Improve customer acquisition.")

if len(recommendations) == 0:
    print("Business is performing very well.")
else:
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec}")



print("\n" + "="*60)
print("        EXECUTIVE SUMMARY")
print("="*60)

print(f"Revenue              : ₹{total_revenue:,.2f}")
print(f"Customers            : {total_customers:,}")
print(f"Orders               : {total_orders:,}")
print(f"Products             : {total_products:,}")
print(f"Sellers              : {total_sellers:,}")

print("-"*60)

print(f"Business Score       : {business_score}/100")
print(f"Business Status      : {status}")

print("="*60)


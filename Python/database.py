import pandas as pd
from sqlalchemy import create_engine

from config import *


def connect_database():

    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(connection_string)

    print("✅ Connected Successfully")

    return engine


def load_tables(engine):

    customers = pd.read_sql("SELECT * FROM customers", engine)

    orders = pd.read_sql("SELECT * FROM orders", engine)

    payments = pd.read_sql("SELECT * FROM payments", engine)

    products = pd.read_sql("SELECT * FROM products", engine)

    sellers = pd.read_sql("SELECT * FROM sellers", engine)

    order_items = pd.read_sql("SELECT * FROM order_items", engine)

    print("✅ Tables Loaded Successfully")

    return (
        customers,
        orders,
        payments,
        products,
        sellers,
        order_items
    )
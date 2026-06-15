import pandas as pd
from sqlalchemy import create_engine

engine=create_engine(
    "postgresql+psycopg2://postgres:root@127.0.0.1:5432/postgres"
)
df = pd.read_sql("SELECT current_database()", engine)


files = {
    "erp_products": r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_products.csv",
    "erp_prod_variants": r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_prod_variants.csv",
    "erp_customers": r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_customers.csv",
    "erp_orders": r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_orders.csv",
    "erp_order_items": r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_order_items.csv"
}

for table_name, file_path in files.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        name=table_name,
        schema="bronze",
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded successfully")
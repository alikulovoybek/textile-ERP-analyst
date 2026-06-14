import pandas as pd
import random
from datetime import datetime, timedelta

# customers list (C001 - C010)
customers = [f"C{str(i).zfill(3)}" for i in range(1, 11)]

statuses = ["Completed", "Pending", "Cancelled"]

start_date = datetime(2024, 1, 1)

orders = []

order_count = 500  # 🔥 KO'P DATA

for i in range(1, order_count + 1):
    order_id = f"O{str(i).zfill(5)}"
    customer_id = random.choice(customers)

    # random date
    random_days = random.randint(0, 365)
    order_date = start_date + timedelta(days=random_days)

    status = random.choices(
        statuses,
        weights=[0.7, 0.2, 0.1]  # ko'p completed bo'lsin
    )[0]

    # temporary total (keyin order_items dan hisoblanadi)
    total_amount = round(random.uniform(500, 10000), 2)

    orders.append([
        order_id,
        customer_id,
        order_date.strftime("%Y-%m-%d"),
        status,
        total_amount
    ])

df_orders = pd.DataFrame(orders, columns=[
    "order_id",
    "customer_id",
    "order_date",
    "status",
    "total_amount"
])

df_orders.to_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_orders.csv", index=False)

print("erp_orders created with", len(df_orders), "rows")
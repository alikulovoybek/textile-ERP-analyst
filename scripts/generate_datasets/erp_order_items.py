import pandas as pd
import random

# load data
orders_df = pd.read_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_orders.csv")
variants_df = pd.read_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_prod_variants.csv")

order_items = []
item_id = 1

for _, order in orders_df.iterrows():

    order_id = order["order_id"]

    # har orderda 1-5 ta product bo'ladi
    num_items = random.randint(1, 5)

    selected_variants = variants_df.sample(num_items)

    for _, var in selected_variants.iterrows():

        quantity = random.randint(50, 2000)  # 🔥 textile realistic

        unit_price = var["unit_cost"]

        line_total = round(quantity * unit_price, 2)

        order_items.append([
            f"OI{str(item_id).zfill(6)}",
            order_id,
            var["variant_id"],
            quantity,
            unit_price,
            line_total
        ])

        item_id += 1


df_items = pd.DataFrame(order_items, columns=[
    "order_item_id",
    "order_id",
    "variant_id",
    "quantity",
    "unit_price",
    "line_total"
])

df_items.to_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_order_items.csv", index=False)

print("order_items created:", len(df_items))
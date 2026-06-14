
#Create erp_prod_variants mock table

import pandas as pd

colors = ["White", "Black", "Blue", "Gray"]
sizes = ["S", "M", "L", "XL", "XXL"]

products = ["P001", "P002", "P003", "P004", "P005", "P006"]

variant_id = 1
variants = []

base_cost = {
    "P001": 5.5,
    "P002": 12.0,
    "P003": 15.0,
    "P004": 8.0,
    "P005": 25.0,
    "P006": 18.0
}

for p in products:
    for color in colors:
        for size in sizes:
            cost = base_cost[p]

            # size bo‘yicha narx farqi
            if size == "XL":
                cost += 0.5
            elif size == "XXL":
                cost += 1

            variants.append([
                f"V{variant_id:03}",
                p,
                color,
                size,
                round(cost, 2)
            ])

            variant_id += 1

df_variants = pd.DataFrame(
    variants,
    columns=["variant_id", "product_id", "color", "size", "unit_cost"]
)

df_variants.to_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_prod_variants.csv", index=False)

print(df_variants.head())
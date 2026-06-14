#Generate Products table by using pandas library

import pandas as pd

masters = [
    ["P001", "Cotton T-Shirt", "T-Shirt", "2024-01-10"],
    ["P002", "Jeans Pant", "Jeans", "2024-01-12"],
    ["P003", "Hoodie", "Hoodie", "2024-01-15"],
    ["P004", "Polo Shirt", "Polo", "2024-01-18"],
    ["P005", "Jacket", "Jacket", "2024-01-20"],
    ["P006", "Sports Set", "Sportswear", "2024-01-22"],
]

df_masters = pd.DataFrame(
    masters,
    columns=["product_id", "product_name", "category", "created_date"]
)

df_masters.to_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_products.csv", index=False)
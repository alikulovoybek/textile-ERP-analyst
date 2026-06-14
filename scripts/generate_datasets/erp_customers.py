# Customer table generated

import pandas as pd

customers = [
    ["C001", "Textile Trade LLC", "Uzbekistan", "Tashkent", "Wholesale", "2024-01-05"],
    ["C002", "Fashion Group", "Kazakhstan", "Almaty", "Retail", "2024-01-06"],
    ["C003", "Global Fabrics", "Turkey", "Istanbul", "Wholesale", "2024-01-07"],
    ["C004", "Premium Wear", "Uzbekistan", "Samarkand", "Retail", "2024-01-08"],
    ["C005", "Cotton Export", "Tajikistan", "Dushanbe", "Wholesale", "2024-01-09"],
    ["C006", "Style House", "Kyrgyzstan", "Bishkek", "Retail", "2024-01-10"],
    ["C007", "Euro Textile", "Germany", "Berlin", "Wholesale", "2024-01-11"],
    ["C008", "Modern Fashion", "UAE", "Dubai", "Retail", "2024-01-12"],
    ["C009", "Silk Road Trade", "Uzbekistan", "Bukhara", "Wholesale", "2024-01-13"],
    ["C010", "Trend Collection", "Kazakhstan", "Astana", "Retail", "2024-01-14"],
]

df = pd.DataFrame(customers, columns=[
    "customer_id",
    "customer_name",
    "country",
    "city",
    "customer_type",
    "created_date"
])

df.to_csv(r"C:\Users\Oybek\textile-ERP-analyst\dataset\raw\erp_customers.csv", index=False)

print("erp_customers created")
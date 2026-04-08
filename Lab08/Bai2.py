import pandas as pd

print("\n--- BÀI 2 ---")
df_sales = pd.read_csv('sales_semicolon.csv', sep=';')
print(df_sales.head(2))
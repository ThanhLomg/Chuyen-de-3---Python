import pandas as pd

print("\n--- BÀI 4 ---")
df_customers = pd.read_csv('customers.csv', dtype={'MaKH': str})
print(df_customers.dtypes)
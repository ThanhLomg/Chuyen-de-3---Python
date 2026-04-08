import pandas as pd

print("\n--- BÀI NC 2: CHUẨN HÓA VÀ NỐI DỮ LIỆU ---")
df_jan = pd.read_csv('sales_jan.csv')
df_feb = pd.read_csv('sales_feb.csv')
df_mar = pd.read_csv('sales_mar.csv')

# Chuẩn hóa: Ép tất cả các DataFrame dùng chung 1 mảng tên cột
chuan_ten_cot = ['MaDH', 'Ngay', 'SanPham', 'DoanhThu']
df_jan.columns = chuan_ten_cot
df_feb.columns = chuan_ten_cot
df_mar.columns = chuan_ten_cot

# Nối dữ liệu (Stack chồng lên nhau)
df_sales_ql = pd.concat([df_jan, df_feb, df_mar], ignore_index=True)

df_sales_ql.to_csv('sales_ql.csv', index=False)
print("Kết quả dữ liệu Quý 1 sau khi nối:\n", df_sales_ql)
print("=> Đã lưu thành công file 'sales_ql.csv'")
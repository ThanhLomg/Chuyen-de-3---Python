import pandas as pd

print("\n--- BÀI 6 & 7 ---")
# Đọc 1 sheet cụ thể
df_hanghoa = pd.read_excel('inventory.xlsx', sheet_name='HangHoa')
print("Sản phẩm tồn < 20:\n", df_hanghoa[df_hanghoa['SoLuongTon'] < 20])

# Đọc toàn bộ các sheet trong file Excel (trả về Dictionary)
dict_sheets = pd.read_excel('inventory.xlsx', sheet_name=None)
print("Các sheet có trong file:", list(dict_sheets.keys()))
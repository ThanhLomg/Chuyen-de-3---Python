import pandas as pd

print("\n--- BÀI 5 ---")
# Đọc file UTF-8 chuẩn
df_sv_utf8 = pd.read_csv('sinhvien_utf8.csv', encoding='utf-8')
print("Đọc thành công dữ liệu UTF-8!")
# Hiển thị dữ liệu
print(df_sv_utf8)   
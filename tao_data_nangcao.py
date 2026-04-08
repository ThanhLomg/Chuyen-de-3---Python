import pandas as pd

# 1. Tạo file scores.xlsx cho Bài NC 1
pd.DataFrame({
    'MaSV': ['SV01', 'SV02', 'SV03', 'SV04'],
    'DiemQT': [7.0, 8.5, 6.0, 9.0],
    'DiemThi': [7.5, 8.0, 6.5, 9.5]
}).to_excel('scores.xlsx', index=False)

# 2. Tạo file orders.xlsx cho Bài NC 5
pd.DataFrame({
    'MaDH': ['DH01', 'DH02', 'DH03', 'DH04'],
    'MaKH': ['0123', '0045', '0123', '0789'],
    'MaSP': ['SP01', 'SP02', 'SP03', 'SP01'],
    'SoLuong': [1, 2, 1, 3],
    'Ngay': ['2026-04-01', '2026-04-02', '2026-04-03', '2026-04-04']
}).to_excel('orders.xlsx', index=False)

print("Đã tạo xong file scores.xlsx và orders.xlsx!")
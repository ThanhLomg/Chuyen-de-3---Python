import pandas as pd

# Đọc file
df = pd.read_csv("lab9/lienhe.csv")

# 1. Chuẩn hóa email (chữ thường)
df['Email'] = df['Email'].str.lower().str.strip()

# 2. Kiểm tra email hợp lệ
df = df[df['Email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', regex=True)]

# 3. Tách domain email
df['Domain'] = df['Email'].str.extract(r'@(.+)')

# 4. Tách đầu số điện thoại (3 số đầu)
df['DauSo'] = df['SoDienThoai'].astype(str).str[:3]

# 5. Xóa khoảng trắng địa chỉ
df['DiaChi'] = df['DiaChi'].str.strip()

# Lưu file
df.to_csv("lab9/clean_bai10.csv", index=False)

print("✅ Đã xử lý xong bài 10")
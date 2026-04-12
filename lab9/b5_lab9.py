import pandas as pd

# Đọc file
df = pd.read_csv("lab9/suckhoe.csv")

# 1. Phát hiện tuổi bất thường
tuoi_loi = df[(df['Tuoi'] <= 0) | (df['Tuoi'] > 100)]
print("📌 Dữ liệu tuổi bất thường:")
print(tuoi_loi)

# 2. Kiểm tra thiếu
print("📌 Giá trị thiếu:")
print(df.isna().sum())

# 3. Điền thiếu bằng median
df['CanNang'] = df['CanNang'].fillna(df['CanNang'].median())
df['ChieuCao'] = df['ChieuCao'].fillna(df['ChieuCao'].median())

# 4. Chuẩn hóa nhóm máu
df['NhomMau'] = df['NhomMau'].str.upper().str.strip()

# 5. Tính BMI
df['BMI'] = df['CanNang'] / ((df['ChieuCao'] / 100) ** 2)

# Lưu file
df.to_csv("lab9/clean_bai5.csv", index=False)

print("✅ Đã xử lý xong bài 5")
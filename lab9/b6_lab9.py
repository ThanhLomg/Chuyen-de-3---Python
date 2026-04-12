import pandas as pd

# Đọc file
df = pd.read_csv("lab9/sanpham.csv")

# 1. Xóa ký tự tiền tệ, dấu phẩy
df['Gia'] = df['Gia'].str.replace(r'[^\d]', '', regex=True).astype(float)

# 2. Chuyển sang số
df['Gia'] = df['Gia'].astype(float)

# 3. Chuẩn hóa danh mục (chữ thường)
df['DanhMuc'] = df['DanhMuc'].str.strip().str.lower()

# 4. Loại sản phẩm tồn kho âm
df = df[df['SoLuongTon'] >= 0]

# 5. Sắp xếp theo giá giảm dần
df = df.sort_values(by='Gia', ascending=False)

# Lưu file
df.to_csv("lab9/clean_bai6.csv", index=False)

print("✅ Đã xử lý xong bài 6")
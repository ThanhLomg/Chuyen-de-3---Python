import pandas as pd

# Đọc file (nhớ đúng thư mục lab9 giống bài 1)
df = pd.read_csv("lab9/donhang.csv")

# 1. Kiểm tra trùng toàn bộ
print("Số dòng trùng toàn bộ:", df.duplicated().sum())

# 2. Kiểm tra trùng theo MaDon
print("Số dòng trùng MaDon:", df.duplicated(subset='MaDon').sum())

# 3. Xóa trùng (giữ dòng đầu)
df = df.drop_duplicates(subset='MaDon', keep='first')

# 4. Tính thành tiền
df['ThanhTien'] = df['SoLuong'] * df['DonGia']

# 5. Sắp xếp theo ngày
df['NgayDat'] = pd.to_datetime(df['NgayDat'])
df = df.sort_values(by='NgayDat')

# Lưu file
df.to_csv("lab9/clean_bai2.csv", index=False)

print("✅ Đã xử lý xong bài 2")
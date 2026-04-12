import pandas as pd

# Đọc file
df = pd.read_csv("lab9/chitieu.csv")

# 1. Kiểm tra giao dịch lỗi
print("📌 Giao dịch không hợp lệ:")
print(df[df['SoTien'] <= 0])

# 2. Loại bỏ dữ liệu lỗi
df = df[df['SoTien'] > 0]

# 3. Phân nhóm mức chi tiêu
df['MucChiTieu'] = pd.cut(
    df['SoTien'],
    bins=[0, 100, 500, 10000],
    labels=['Thap', 'TrungBinh', 'Cao']
)

# 4. Thống kê số giao dịch theo mức
print("📊 Số giao dịch theo mức:")
print(df['MucChiTieu'].value_counts())

# 5. Tổng chi tiêu theo nhóm
tong_chi = df.groupby('NhomChiTieu')['SoTien'].sum()
print("💰 Tổng chi theo nhóm:")
print(tong_chi)

# Lưu file
df.to_csv("lab9/clean_bai8.csv", index=False)

print("✅ Đã xử lý xong bài 8")
import pandas as pd

# Đọc file
df = pd.read_csv("lab9/nhansu.csv")

# 1. Chuẩn hóa giới tính
df['GioiTinh'] = df['GioiTinh'].replace({
    'nam': 'Nam',
    'NAM': 'Nam',
    'Nam': 'Nam',
    'nu': 'Nữ',
    'nữ': 'Nữ',
    'Nữ': 'Nữ'
})

# 2. Chuẩn hóa phòng ban (viết hoa chữ cái đầu)
df['PhongBan'] = df['PhongBan'].str.strip().str.title()

# 3. Xóa khoảng trắng thừa trong họ tên
df['HoTen'] = df['HoTen'].str.strip()

# 4. Đổi tên cột
df = df.rename(columns={
    'MaNV': 'ma_nv',
    'HoTen': 'ho_ten',
    'GioiTinh': 'gioi_tinh',
    'PhongBan': 'phong_ban',
    'Luong': 'luong'
})

# Lưu file
df.to_csv("lab9/clean_bai3.csv", index=False)

print("✅ Đã xử lý xong bài 3")
import pandas as pd

# Đọc file
df = pd.read_csv("lab9/khaosat.csv")

# 1. Chuẩn hóa cột CoLamThem về 1/0
df['CoLamThem'] = df['CoLamThem'].replace({
    'Yes': 1, 'No': 0,
    'Có': 1, 'Không': 0,
    'Y': 1, 'N': 0
})

# 2. Chuẩn hóa MucDoHaiLong (ví dụ nếu dạng chữ)
df['MucDoHaiLong'] = df['MucDoHaiLong'].replace({
    'Rất hài lòng': 5,
    'Hài lòng': 4,
    'Bình thường': 3,
    'Không hài lòng': 2,
    'Rất không hài lòng': 1
})

# 3. Đổi tên cột
df = df.rename(columns={
    'MaSV': 'ma_sv',
    'GioHocMoiNgay': 'gio_hoc',
    'MucDoHaiLong': 'hai_long',
    'CoLamThem': 'co_lam_them'
})

# 4. Loại dữ liệu lỗi
df = df[df['gio_hoc'] >= 0]

# 5. Thống kê
print("📊 Số SV làm thêm / không:")
print(df['co_lam_them'].value_counts())

# Lưu file
df.to_csv("lab9/clean_bai7.csv", index=False)

print("✅ Đã xử lý xong bài 7")
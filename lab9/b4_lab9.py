import pandas as pd

# Đọc file
df = pd.read_csv("lab9/muonsach.csv")

# 1. Chuyển về datetime
df['NgayMuon'] = pd.to_datetime(df['NgayMuon'])
df['NgayTra'] = pd.to_datetime(df['NgayTra'])

# 2. Giữ nguyên bản ghi chưa trả (NaT vẫn giữ)

# 3. Chuẩn hóa trạng thái
df['TrangThai'] = df['TrangThai'].replace({
    'đã trả': 'DaTra',
    'Đã trả': 'DaTra',
    'chưa trả': 'ChuaTra',
    'Chưa trả': 'ChuaTra'
})

# 4. Tính số ngày mượn
df['SoNgayMuon'] = (df['NgayTra'] - df['NgayMuon']).dt.days

# 5. Liệt kê sinh viên mượn quá 30 ngày
qua_han = df[df['SoNgayMuon'] > 30]
print("📌 Sinh viên mượn quá hạn:")
print(qua_han)

# Lưu file
df.to_csv("lab9/clean_bai4.csv", index=False)

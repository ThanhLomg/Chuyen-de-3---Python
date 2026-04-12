import pandas as pd

df = pd.read_csv("lab9/diem_sinhvien.csv")
# Kiểm tra thiếu
print(df.isna().sum())

# Điền điểm thiếu bằng trung bình
df['DiemQT'] = df['DiemQT'].fillna(df['DiemQT'].mean())
df['DiemThi'] = df['DiemThi'].fillna(df['DiemThi'].mean())

# Điền tên thiếu
df['HoTen'] = df['HoTen'].fillna("ChuaCapNhat")

# Tính điểm tổng kết
df['DiemTK'] = 0.4 * df['DiemQT'] + 0.6 * df['DiemThi']

# Xếp loại
def xeploai(d):
    if d >= 8: return 'A'
    elif d >= 6.5: return 'B'
    elif d >= 5: return 'C'
    else: return 'D'

df['XepLoai'] = df['DiemTK'].apply(xeploai)

df.to_csv("clean_bai1.csv", index=False)
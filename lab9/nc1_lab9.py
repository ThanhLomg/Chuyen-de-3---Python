import pandas as pd

# Đọc file (ĐÚNG)
df = pd.read_csv("sinhvien.csv")

# Tính điểm TB
df['DiemTB'] = (df['DiemQT'] + df['DiemGK'] + df['DiemCK']) / 3

# Xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "Gioi"
    elif diem >= 6.5:
        return "Kha"
    elif diem >= 5:
        return "TrungBinh"
    else:
        return "Yeu"

df['XepLoai'] = df['DiemTB'].apply(xep_loai)

# Top 3
top3 = df.nlargest(3, 'DiemTB')
print(top3)

# Lưu file
df.to_csv("nc_bai1.csv", index=False)

print("✅ Done")
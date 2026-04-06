import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

# Tính điểm trung bình
df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

print(df[["HoTen", "DiemTB", "XepLoai"]])
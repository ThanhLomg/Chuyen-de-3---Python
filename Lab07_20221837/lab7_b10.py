import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

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

pivot1 = pd.pivot_table(
    df,
    index="Lop",
    columns="XepLoai",
    values="MaSV",
    aggfunc="count",
    fill_value=0
)

print("=== Pivot Table: Lớp vs Xếp loại ===")
print(pivot1)
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

print("Giới tính:")
print(df["GioiTinh"].value_counts())

print("\nLớp:")
print(df["Lop"].value_counts())

print("\nChuyên ngành:")
print(df["ChuyenNganh"].value_counts())

print("\nXếp loại:")
print(df["XepLoai"].value_counts())
import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

bins = [0, 5, 7, 8.5, 10]
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]

df["NhomDiem"] = pd.cut(df["DiemTB"], bins=bins, labels=labels, right=False)

bang_nhom = pd.crosstab(df["Lop"], df["NhomDiem"])

print("=== Thống kê nhóm điểm theo lớp ===")
print(bang_nhom)
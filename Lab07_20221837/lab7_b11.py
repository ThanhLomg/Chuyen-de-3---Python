import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

bang_cheo = pd.crosstab(df["Lop"], df["GioiTinh"])

print("=== Bảng chéo: Lớp vs Giới tính ===")
print(bang_cheo)
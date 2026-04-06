import pandas as pd
import numpy as np

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Do", "Truot")

so_luong = pd.crosstab(df["Lop"], df["KetQua"])

print("=== Số lượng Đỗ / Trượt theo lớp ===")
print(so_luong)

ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index") * 100

print("\n=== Tỷ lệ Đỗ / Trượt (%) theo lớp ===")
print(ty_le.round(2))
import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

tb_theo_lop = df.groupby("Lop")["DiemTB"].mean()

print("=== Điểm trung bình theo lớp ===")
print(tb_theo_lop)
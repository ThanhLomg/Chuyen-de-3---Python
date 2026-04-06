import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

tonghop = df.groupby("Lop")["DiemTB"].agg(["count", "mean", "max", "min"])

print("=== Tổng hợp theo lớp ===")
print(tonghop)
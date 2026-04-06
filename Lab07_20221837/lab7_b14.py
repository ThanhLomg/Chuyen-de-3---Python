import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

idx = df.groupby("Lop")["DiemTB"].idxmax()

sv_max = df.loc[idx, ["HoTen", "Lop", "DiemTB"]]

print("=== Sinh viên có điểm cao nhất mỗi lớp ===")
print(sv_max)
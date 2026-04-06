import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

tb_theo_gt = df.groupby("GioiTinh")["DiemTB"].mean()

print("=== Điểm trung bình theo giới tính ===")
print(tb_theo_gt)
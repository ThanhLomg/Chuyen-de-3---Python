import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

print("\n=== Danh sách điểm trung bình ===")
print(df[["MaSV", "HoTen", "DiemTB"]])

print("\nTrung bình:", df["DiemTB"].mean())
print("Lớn nhất:", df["DiemTB"].max())
print("Nhỏ nhất:", df["DiemTB"].min())
print("Độ lệch chuẩn:", df["DiemTB"].std())
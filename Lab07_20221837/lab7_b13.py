import pandas as pd

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

df["DiemTB"] = (df["DiemQT"] + df["DiemGK"] + df["DiemCK"]) / 3

df["XepHangTrongLop"] = df.groupby("Lop")["DiemTB"].rank(
    ascending=False,
    method="dense"
)

ketqua = df[["HoTen", "Lop", "DiemTB", "XepHangTrongLop"]] \
    .sort_values(["Lop", "XepHangTrongLop"])

print("=== Xếp hạng sinh viên trong từng lớp ===")
print(ketqua)
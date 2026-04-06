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

tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)

tyle_ab = df[df["XepLoai"].isin(["A", "B"])] \
    .groupby("ChuyenNganh")["MaSV"].count()

tong_hop_cn["SoDatAB"] = tyle_ab

tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)

tong_hop_cn["TyLeDatAB"] = tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"] * 100

print("=== Báo cáo theo chuyên ngành ===")
print(tong_hop_cn.round(2))
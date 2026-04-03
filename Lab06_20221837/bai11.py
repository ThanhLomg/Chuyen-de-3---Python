import pandas as pd

print("--- BÀI 11: NHẬP - XUẤT - TỒN ---")
data = {
    "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06"],
    "TenSP": ["Laptop", "Chuot", "Ban phim", "USB", "Loa", "Webcam"],
    "TonDau": [5, 20, 15, 30, 10, 8],
    "NhapThem": [3, 10, 5, 20, 4, 2],
    "DaBan": [4, 18, 12, 35, 9, 3],
    "DonGia": [14500000, 150000, 300000, 180000, 750000, 900000]
}
df = pd.DataFrame(data)

df["TonCuoi"] = df["TonDau"] + df["NhapThem"] - df["DaBan"]
df["GiaTriTonCuoi"] = df["TonCuoi"] * df["DonGia"]

print("1. Bảng dữ liệu kho hàng:")
print(df)

print("\n2. Sản phẩm sắp hết hàng (Tồn cuối <= 5):")
print(df[df["TonCuoi"] <= 5])

print("\n3. Sản phẩm có giá trị tồn cuối lớn nhất:")
print(df.loc[df["GiaTriTonCuoi"].idxmax()])
print("-" * 50)
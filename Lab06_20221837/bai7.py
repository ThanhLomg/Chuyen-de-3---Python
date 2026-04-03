import pandas as pd

print("--- BÀI 7: QUẢN LÝ DANH SÁCH SẢN PHẨM ---")
data = {
    "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06", "SP07", "SP08"],
    "TenSP": ["Chuot", "Ban phim", "Man hinh", "USB", "Laptop", "Loa", "Tai nghe", "Webcam"],
    "LoaiHang": ["Phu kien", "Phu kien", "Thiet bi", "Phu kien", "Thiet bi", "Thiet bi", "Phu kien", "Thiet bi"],
    "DonGia": [150000, 300000, 2500000, 180000, 14500000, 750000, 450000, 900000],
    "SoLuongTon": [25, 18, 7, 40, 5, 12, 20, 8]
}
df = pd.DataFrame(data)

print("1. Sản phẩm có đơn giá > 500,000:")
print(df[df["DonGia"] > 500000])

df["GiaTriTonKho"] = df["DonGia"] * df["SoLuongTon"]
print("\n2. Sắp xếp theo giá trị tồn kho giảm dần:")
print(df.sort_values(by="GiaTriTonKho", ascending=False))

print("\n3. Sản phẩm có số lượng tồn < 10:")
print(df[df["SoLuongTon"] < 10])
print("-" * 50)
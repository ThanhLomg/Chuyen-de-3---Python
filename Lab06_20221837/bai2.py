import pandas as pd

print("--- BÀI 2: TẠO DATAFRAME TỪ DICT ---")
# Khởi tạo dữ liệu
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
    "HoTen": ["An", "Bình", "Chi", "Dũng", "Hà"],
    "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1"],
    "DiemQT": [7.0, 8.5, 6.0, 9.0, 8.0],
    "DiemThi": [7.5, 8.0, 6.5, 9.5, 8.5]
}
df = pd.DataFrame(data)

print("1. Hiển thị toàn bộ DataFrame:")
print(df)

print("\n2. Chọn cột HoTen và DiemThi:")
print(df[["HoTen", "DiemThi"]])

# Thêm cột điểm trung bình
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

print("\n3. DataFrame sau khi thêm cột DiemTB:")
print(df)
print("-" * 50)
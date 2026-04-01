import pandas as pd
import numpy as np

print("--- BÀI 6: QUY TRÌNH LÀM SẠCH VÀ CHUẨN HÓA DỮ LIỆU ---")

# Khởi tạo dữ liệu thô ban đầu
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10", "SV11", "SV12", "SV13", "SV14", "SV15"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20, 21, 20, 19, 18, 22, 21, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None, "NỮ", "Nam", "Nữ", "Nam", "Nữ", "Nam", "Nữ"],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5, 2.5, 3, 4, 2, 3, 2.5, None],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 2, 5, 20, None, 4, 5, 3.5, 3.5, 2, 5, 20],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None, 3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5]
}
df = pd.DataFrame(data)

# 1. In dữ liệu ban đầu và kích thước
print("1. Kích thước bộ dữ liệu ban đầu:", df.shape)

# 2. Kiểm tra số lượng giá trị thiếu
print("\n2. Số lượng giá trị thiếu ở từng cột:\n", df.isnull().sum())

# 3. Xóa bản ghi trùng lặp
df = df.drop_duplicates(subset="MaSV")

# 4. Chuẩn hóa cột Giới tính
df["GioiTinh"] = df["GioiTinh"].replace({"nu": "Nữ", "NỮ": "Nữ", "Nam": "Nam"})
df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# 5. Điền dữ liệu thiếu (NA) bằng giá trị trung bình
cols_to_fill = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]
for col in cols_to_fill:
    df[col] = df[col].fillna(df[col].mean())

# 6 & 7. Phát hiện và xử lý dữ liệu bất thường (thay bằng trung bình)
df.loc[df["Tuoi"] > 30, "Tuoi"] = df["Tuoi"].mean()
df.loc[df["GioTuHoc"] < 0, "GioTuHoc"] = df["GioTuHoc"].mean()
df.loc[df["GioMangXaHoi"] > 12, "GioMangXaHoi"] = df["GioMangXaHoi"].mean()
df.loc[df["DiemTB"] > 4.0, "DiemTB"] = df["DiemTB"].mean()

# 8. In bộ dữ liệu sau làm sạch
print("\n8. DỮ LIỆU SAU KHI LÀM SẠCH:\n", np.round(df, 2))

# 9. Chuẩn hóa Min-Max
df_minmax = df.copy()
for col in cols_to_fill:
    df_minmax[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
print("\n9. DỮ LIỆU SAU CHUẨN HÓA MIN-MAX [0, 1]:\n", np.round(df_minmax[cols_to_fill], 2))

# 10. Chuẩn hóa Z-score
df_zscore = df.copy()
for col in cols_to_fill:
    df_zscore[col] = (df[col] - df[col].mean()) / df[col].std()
print("\n10. DỮ LIỆU SAU CHUẨN HÓA Z-SCORE:\n", np.round(df_zscore[cols_to_fill], 2))
print("-" * 50)
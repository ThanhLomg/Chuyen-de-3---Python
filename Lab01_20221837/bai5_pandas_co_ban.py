import pandas as pd

# Tạo dữ liệu dictionary
data = {
    "MaSV": ["SV01", "SV02", "SV03"],
    "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C"],
    "Lop": ["CNTT1", "CNTT1", "CNTT2"],
    "Diem": [8.0, 7.5, 9.0]
}

df = pd.DataFrame(data)

print("--- Toàn bộ bảng dữ liệu ---")
print(df)

print("\n--- 2 dòng đầu tiên ---")
print(df.head(2))

print("\n--- Tên các cột ---")
print(list(df.columns))

diem_tb = df["Diem"].mean()
print(f"\n--- Điểm trung bình của cột Điểm: {diem_tb:.2f} ---")
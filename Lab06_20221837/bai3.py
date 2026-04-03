import pandas as pd

print("--- BÀI 3: ĐỌC FILE CSV VÀ KHÁM PHÁ DỮ LIỆU ---")
try:
    df = pd.read_csv("diem_sinhvien.csv")

    print("1. 5 dòng đầu tiên:")
    print(df.head())

    print("\n2. 5 dòng cuối cùng:")
    print(df.tail())

    print("\n3. Kích thước dữ liệu (dòng, cột):", df.shape)
    print("4. Tên các cột:", df.columns.tolist())

    print("\n5. Thông tin dữ liệu (info):")
    df.info()

    print("\n6. Thống kê mô tả (describe):")
    print(df.describe())
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'diem_sinhvien.csv'. Hãy kiểm tra lại!")
print("-" * 50)
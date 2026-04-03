import pandas as pd

print("--- BÀI 4: TIỀN XỬ LÝ DATAFRAME ---")
try:
    df = pd.read_csv("diem_sinhvien.csv")

    # Tính điểm trung bình
    df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

    print("1. Danh sách sinh viên có DiemTB >= 8:")
    print(df[df["DiemTB"] >= 8])

    # Hàm xếp loại
    def xep_loai(diem):
        if diem >= 8.5:
            return "Gioi"
        elif diem >= 7.0:
            return "Kha"
        elif diem >= 5.5:
            return "Trung binh"
        else:
            return "Yeu"

    # Áp dụng hàm xếp loại vào cột DiemTB
    df["XepLoai"] = df["DiemTB"].apply(xep_loai)

    # Đổi tên cột HoTen thành TenSinhVien
    df = df.rename(columns={"HoTen": "TenSinhVien"})

    # Thiết lập MaSV làm index
    df = df.set_index("MaSV")

    print("\n2. Bảng dữ liệu cuối cùng sau khi xử lý:")
    print(df)
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'diem_sinhvien.csv'!")
print("-" * 50)
import pandas as pd

print("--- BÀI 6: BÀI TẬP TỔNG HỢP ---")
try:
    # 1. Đọc dữ liệu
    df = pd.read_csv("diem_sinhvien.csv")
    
    # 2. Tính DiemTB
    df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

    # 3. Tính XepLoai
    def xep_loai(diem):
        if diem >= 8.5:
            return "Gioi"
        elif diem >= 7.0:
            return "Kha"
        elif diem >= 5.5:
            return "Trung binh"
        else:
            return "Yeu"

    df["XepLoai"] = df["DiemTB"].apply(xep_loai)

    # 4. Lọc sinh viên Khá, Giỏi và sắp xếp DiemTB giảm dần
    ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]
    ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)

    # 5. Lưu kết quả ra file CSV
    ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")

    print("Đã hoàn tất xử lý và lưu danh sách đạt yêu cầu vào file 'ketqua_xuly.csv' thành công!")
    print("\nKết quả danh sách Khá/Giỏi:")
    print(ket_qua)

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'diem_sinhvien.csv'. Bạn kiểm tra lại nhé!")
print("-" * 50)
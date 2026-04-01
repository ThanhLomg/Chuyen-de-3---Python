# BÀI 5: ĐỌC FILE VĂN BẢN VÀ THỐNG KÊ DỮ LIỆU

def doc_va_thong_ke():
    ds_sinh_vien = []
    
    # 1. Đọc dữ liệu từ file sinhvien.txt
    try:
        with open('sinhvien.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # Cắt chuỗi theo dấu phẩy và xóa khoảng trắng thừa
                parts = line.strip().split(',')
                if len(parts) == 3:
                    ma_sv = parts[0].strip()
                    ho_ten = parts[1].strip()
                    diem = float(parts[2].strip())
                    ds_sinh_vien.append({'ma_sv': ma_sv, 'ho_ten': ho_ten, 'diem': diem})
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'sinhvien.txt'. Vui lòng tạo file trước!")
        return

    # 2. Tính toán thống kê
    so_luong = len(ds_sinh_vien)
    if so_luong == 0:
        print("Không có dữ liệu hợp lệ để thống kê.")
        return

    tong_diem = sum(sv['diem'] for sv in ds_sinh_vien)
    diem_tb = tong_diem / so_luong
    so_dat = sum(1 for sv in ds_sinh_vien if sv['diem'] >= 5.0)
    so_khong_dat = so_luong - so_dat

    # 3. Ghi kết quả ra file baocao.txt
    with open('baocao.txt', 'w', encoding='utf-8') as f:
        f.write("BÁO CÁO THỐNG KÊ KẾT QUẢ HỌC TẬP\n")
        f.write("===================================\n")
        f.write(f"Tổng số sinh viên: {so_luong}\n")
        f.write(f"Điểm trung bình: {diem_tb:.2f}\n")
        f.write(f"Số sinh viên đạt: {so_dat}\n")
        f.write(f"Số sinh viên không đạt: {so_khong_dat}\n")
        f.write("===================================\n")

    print("Hoàn tất! Đã đọc file 'sinhvien.txt' và ghi báo cáo ra file 'baocao.txt'.")

# Gọi hàm chạy chương trình
if __name__ == "__main__":
    doc_va_thong_ke()
import csv

# BÀI 6: ĐỌC FILE CSV VÀ XỬ LÝ LỖI

def xu_ly_file_csv():
    danh_sach_hop_le = []
    danh_sach_loi = []

    # 1. Đọc file và lọc dữ liệu
    try:
        with open('diemlop.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader) # Bỏ qua dòng tiêu đề (MaSV, HoTen, Diem)
            
            for row in reader:
                # Bỏ qua nếu dòng bị trống hoặc thiếu cột
                if len(row) < 3:
                    continue 
                
                ma_sv = row[0].strip()
                ho_ten = row[1].strip()
                diem_str = row[2].strip()
                
                # Kiểm tra lỗi bằng try/except
                try:
                    diem = float(diem_str)
                    if 0 <= diem <= 10:
                        # Nếu điểm hợp lệ (từ 0 đến 10)
                        danh_sach_hop_le.append({'ma_sv': ma_sv, 'ho_ten': ho_ten, 'diem': diem})
                    else:
                        # Nếu điểm là số nhưng ngoài khoảng 0-10
                        danh_sach_loi.append(f"{ma_sv}, {ho_ten}, {diem_str} - Lỗi: Điểm ngoài khoảng 0-10")
                except ValueError:
                    # Nếu điểm chứa chữ cái, không thể ép kiểu sang float
                    danh_sach_loi.append(f"{ma_sv}, {ho_ten}, {diem_str} - Lỗi: Điểm không phải là số")
                    
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'diemlop.csv'. Vui lòng kiểm tra lại!")
        return

    # 2. Tính điểm trung bình của các dòng hợp lệ
    if danh_sach_hop_le:
        tong_diem = sum(sv['diem'] for sv in danh_sach_hop_le)
        diem_tb = tong_diem / len(danh_sach_hop_le)
        print("--- KẾT QUẢ XỬ LÝ DỮ LIỆU ---")
        print(f"Số lượng sinh viên hợp lệ: {len(danh_sach_hop_le)}")
        print(f"Điểm trung bình của danh sách hợp lệ: {diem_tb:.2f}")
    else:
        print("Không có dữ liệu sinh viên nào hợp lệ để tính toán.")

    # 3. Ghi các dòng lỗi vào file loi.txt
    if danh_sach_loi:
        with open('loi.txt', mode='w', encoding='utf-8') as file_loi:
            file_loi.write("DANH SÁCH CÁC DÒNG BỊ LỖI\n")
            file_loi.write("=========================\n")
            for loi in danh_sach_loi:
                file_loi.write(loi + "\n")
        print(f"\nPhát hiện {len(danh_sach_loi)} dòng lỗi! Đã xuất chi tiết ra file 'loi.txt'.")
    else:
        print("\nTuyệt vời! Dữ liệu sạch 100%, không có lỗi nào.")

# Chạy chương trình chính
if __name__ == "__main__":
    xu_ly_file_csv()
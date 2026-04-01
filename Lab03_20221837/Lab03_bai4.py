# BÀI 4: VIẾT HÀM XỬ LÝ DỮ LIỆU SINH VIÊN

def nhap_danh_sach():
    ds_sinh_vien = []
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\n--- Sinh viên thứ {i+1} ---")
        ma_sv = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        diem = float(input("Điểm: "))
        # Lưu thông tin dưới dạng dictionary
        ds_sinh_vien.append({'ma_sv': ma_sv, 'ho_ten': ho_ten, 'diem': diem})
    return ds_sinh_vien

def tinh_diem_trung_binh(ds):
    if len(ds) == 0:
        return 0
    tong_diem = sum(sv['diem'] for sv in ds)
    return tong_diem / len(ds)

def tim_sv_max(ds):
    if len(ds) == 0:
        return None
    sv_max = ds[0]
    for sv in ds:
        if sv['diem'] > sv_max['diem']:
            sv_max = sv
    return sv_max

def xep_loai(diem):
    if diem >= 8.0:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5.0:
        return "C"
    else:
        return "F"

def in_bao_cao(ds):
    print("\n=======================================================")
    print("               BÁO CÁO KẾT QUẢ HỌC TẬP                 ")
    print("=======================================================")
    print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm':<5} | {'Xếp loại':<10}")
    print("-" * 55)
    
    for sv in ds:
        loai = xep_loai(sv['diem'])
        print(f"{sv['ma_sv']:<10} | {sv['ho_ten']:<20} | {sv['diem']:<5.1f} | {loai:<10}")

    dtb = tinh_diem_trung_binh(ds)
    sv_max = tim_sv_max(ds)

    print("-" * 55)
    print(f"Điểm trung bình của lớp: {dtb:.2f}")
    if sv_max:
        print(f"Sinh viên cao điểm nhất: {sv_max['ho_ten']} ({sv_max['diem']} điểm)")
    print("=======================================================")

# CHƯƠNG TRÌNH CHÍNH
if __name__ == "__main__":
    danh_sach = nhap_danh_sach()
    if danh_sach:
        in_bao_cao(danh_sach)
    else:
        print("Danh sách trống!")
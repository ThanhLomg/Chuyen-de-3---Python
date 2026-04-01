print("\n--- BÀI 3: XẾP LOẠI HỌC LỰC ---")
ho_ten = "Phan Thanh Long" 
ma_sv = "20221837"
lop = "DCCNTT13.10.10"
diem_cc = 8.5
diem_gk = 7.0
diem_ck = 8.0

tong_ket = 0.1 * diem_cc + 0.3 * diem_gk + 0.6 * diem_ck
print("Họ tên:", ho_ten)
print("Mã sinh viên:", ma_sv)
print("Lớp:", lop)
print("Điểm tổng kết của bạn là:", round(tong_ket, 2))

if tong_ket >= 8.5:
    xep_loai = "Giỏi"
elif tong_ket >= 7.0:
    xep_loai = "Khá"
elif tong_ket >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Chưa đạt"

print("Với mức điểm trên, bạn xếp loại:", xep_loai)
# bai3_tinh_diem.py
ho_ten = input("Nhập họ tên sinh viên: ")
diem_qt = float(input("Nhập điểm quá trình: "))
diem_thi = float(input("Nhập điểm thi: "))

diem_tb = 0.4 * diem_qt + 0.6 * diem_thi

print(f"\nSinh viên: {ho_ten}")
print(f"Điểm trung bình: {diem_tb:.2f}")

if diem_tb >= 8.0:
    xep_loai = "Giỏi"
elif diem_tb >= 6.5:
    xep_loai = "Khá"
elif diem_tb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Chưa đạt"

print(f"Xếp loại: {xep_loai}")
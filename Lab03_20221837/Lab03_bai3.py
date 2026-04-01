# Bài 3. Sử dụng list/dict comprehension 
print("\n--- BÀI 3: COMPREHENSION ---")
diem_mau = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

# Tạo list mới gồm các điểm đạt (>= 5)
diem_dat = [d for d in diem_mau if d >= 5]
print(f"1. Danh sách điểm đạt: {diem_dat}")

# Tạo list bình phương của các điểm đạt
binh_phuong = [round(d**2, 2) for d in diem_dat]
print(f"2. Bình phương các điểm đạt: {binh_phuong}")

# Tạo dict xếp loại theo STT
xep_loai_dict = {
    i + 1: ("A" if d >= 8 else "B" if d >= 6.5 else "C" if d >= 5 else "F")
    for i, d in enumerate(diem_mau)
}
print(f"3. Từ điển xếp loại (STT: Loại): {xep_loai_dict}")
print("\n--- BÀI 7: THỐNG KÊ KẾT QUẢ ---")
ten = ["An", "Binh", "Chi", "Dung"]
diem = [7.5, 8.0, 6.5, 9.0]
tong = 0
dem_dat = 0

for i in range(len(ten)):
    print(ten[i], "-", diem[i])
    tong += diem[i]
    if diem[i] >= 5:
        dem_dat += 1

dtb = tong / len(diem)
max_diem = max(diem)
vi_tri = diem.index(max_diem)

print("Điểm trung bình:", dtb)
print("Sinh viên cao nhất:", ten[vi_tri])
print("Số sinh viên đạt:", dem_dat)

if dtb >= 8:
    print("Kết luận: Lớp học tốt")
elif dtb >= 6.5:
    print("Kết luận: Lớp học khá")
else:
    print("Kết luận: Cần cải thiện")
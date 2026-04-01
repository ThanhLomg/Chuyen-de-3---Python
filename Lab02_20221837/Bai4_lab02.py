print("\n--- BÀI 4: DUYỆT DANH SÁCH ĐIỂM ---")
diem = [7.5, 8.0, 4.5, 6.0, 9.0, 5.5, 3.5] 
tong = 0
dem_dat = 0

print("Các điểm trong danh sách:")
for x in diem:
    print(x)
    tong += x
    if x >= 5: 
        dem_dat += 1

dtb = tong / len(diem) 
print("Điểm trung bình:", round(dtb, 2))
print("Điểm lớn nhất:", max(diem))
print("Số điểm đạt:", dem_dat)
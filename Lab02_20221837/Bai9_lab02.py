print("\n--- BÀI 9: BÁO CÁO CÓ KIỂM TRA ĐẦU VÀO ---")
n = int(input("Nhập số lượng sinh viên: "))

ten = []
diem = []

for i in range(n):
    ho_ten = input("Nhập họ tên sinh viên thứ " + str(i+1) + ": ")
    x = float(input("Nhập điểm: "))

    while x < 0 or x > 10:
        print("Điểm không hợp lệ. Nhập lại!")
        x = float(input("Nhập điểm: "))

    ten.append(ho_ten)
    diem.append(x)

tong = 0
dem_dat = 0

for i in range(n):
    print(ten[i], "-", diem[i])
    tong += diem[i]
    if diem[i] >= 5:
        dem_dat += 1

dtb = tong / n
max_diem = max(diem)
min_diem = min(diem)
vi_tri_max = diem.index(max_diem)
vi_tri_min = diem.index(min_diem)

print("Sinh viên cao nhất:", ten[vi_tri_max], "-", max_diem)
print("Sinh viên thấp nhất:", ten[vi_tri_min], "-", min_diem)
print("Số sinh viên đạt:", dem_dat)
print("Điểm trung bình:", round(dtb, 2))

if dtb >= 8:
    print("Nhận xét: Lớp học tốt")
elif dtb >= 6.5:
    print("Nhận xét: Lớp học khá")
else:
    print("Nhận xét: Cần cải thiện")
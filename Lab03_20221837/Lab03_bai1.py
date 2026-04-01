# Bài 1. Quản lý danh sách điểm sinh viên bằng list và tuple
print("--- BÀI 1: DANH SÁCH BẰNG LIST VÀ TUPLE ---")
# Khởi tạo danh sách 8 sinh viên (Mã, Họ Tên, Điểm)
ds_sinh_vien = [
    ("SV01", "Phan Thanh Long", 8.5),
    ("SV02", "Tran Thi Binh", 9.2),
    ("SV03", "Le Van Cuong", 7.0),
    ("SV04", "Pham Thi Dung", 4.5),
    ("SV05", "Hoang Van E", 8.0),
    ("SV06", "Vu Thi Hoa", 6.5),
    ("SV07", "Ngo Van Giang", 5.0),
    ("SV08", "Dao Thi Hanh", 9.5)
]

print("1. Toàn bộ danh sách sinh viên:")
for sv in ds_sinh_vien:
    print(sv)

# Tìm sinh viên điểm cao nhất
diem_max = ds_sinh_vien[0][2]
sv_max = ds_sinh_vien[0]
for sv in ds_sinh_vien:
    if sv[2] > diem_max:
        diem_max = sv[2]
        sv_max = sv
print(f"\n2. Sinh viên cao điểm nhất: {sv_max[1]} ({sv_max[2]} điểm)")

# Tính điểm trung bình của lớp
tong_diem = sum(sv[2] for sv in ds_sinh_vien)
diem_tb = tong_diem / len(ds_sinh_vien)
print(f"3. Điểm trung bình của lớp: {round(diem_tb, 2)}")

# Danh sách sinh viên điểm >= 8
print("\n4. Sinh viên có điểm >= 8.0:")
for sv in ds_sinh_vien:
    if sv[2] >= 8.0:
        print(f"- {sv[1]}: {sv[2]}")
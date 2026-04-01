# Bài 2. Thống kê dữ liệu bằng dict và set
print("\n--- BÀI 2: THỐNG KÊ BẰNG DICT VÀ SET ---")
mon_hoc = ["Web Dev", "Python", "Social Work", "Python", "Photoshop", "Web Dev", "Python", "Social Work"]

# Loại bỏ phần tử trùng lặp bằng set
mon_duy_nhat = set(mon_hoc)
print(f"1. Các môn học độc lập: {mon_duy_nhat}")

# Đếm số lần xuất hiện bằng dict
thong_ke = {}
for mon in mon_hoc:
    if mon in thong_ke:
        thong_ke[mon] += 1
    else:
        thong_ke[mon] = 1
print(f"2. Thống kê số lượt đăng ký: {thong_ke}")

# In ra môn học được đăng ký nhiều nhất
mon_max = max(thong_ke, key=thong_ke.get)
print(f"3. Môn học đăng ký nhiều nhất: {mon_max} ({thong_ke[mon_max]} lượt)")

# Sắp xếp kết quả đếm giảm dần
thong_ke_sap_xep = dict(sorted(thong_ke.items(), key=lambda item: item[1], reverse=True))
print(f"4. Sắp xếp giảm dần: {thong_ke_sap_xep}")
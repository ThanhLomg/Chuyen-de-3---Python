import numpy as np

print("--- BÀI 1: THỐNG KÊ MÔ TẢ TRÊN DỮ LIỆU ĐIỂM ---")

# Khởi tạo ma trận điểm (5 sinh viên, 4 môn học)
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# 1. In ra ma trận điểm
print("1. Ma trận điểm:\n", scores)

# 2. Tính điểm trung bình của toàn bộ ma trận
print("\n2. Điểm trung bình toàn bộ:", np.mean(scores))

# 3. Tính điểm trung bình theo từng sinh viên (axis=1: tính theo hàng)
avg_students = np.mean(scores, axis=1)
print("\n3. Điểm trung bình từng sinh viên:", avg_students)

# 4. Tính điểm trung bình theo từng môn (axis=0: tính theo cột)
print("\n4. Điểm trung bình từng môn:", np.mean(scores, axis=0))

# 5. Tìm điểm cao nhất và thấp nhất trong ma trận
print(f"\n5. Điểm cao nhất: {np.max(scores)}")
print(f"   Điểm thấp nhất: {np.min(scores)}")

# 6. Tính độ lệch chuẩn theo từng môn (axis=0)
# Sử dụng np.round để làm tròn 2 chữ số thập phân cho dễ nhìn
print("\n6. Độ lệch chuẩn từng môn:", np.round(np.std(scores, axis=0), 2))

# 7. Xác định sinh viên có điểm trung bình cao nhất
best_student_idx = np.argmax(avg_students)
print(f"\n7. Sinh viên có điểm TB cao nhất là sinh viên thứ {best_student_idx + 1} (Vị trí index: {best_student_idx})")

print("-" * 50)
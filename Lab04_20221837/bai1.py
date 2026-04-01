import numpy as np

print("--- BÀI 1: PHÂN TÍCH ĐIỂM HỌC PHẦN (GIÁO DỤC) ---")

# 1. Tạo ma trận điểm và in thông tin
scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])
print("1. Thông tin ma trận điểm:")
print(f"- Shape: {scores.shape}, Số chiều (ndim): {scores.ndim}, Kiểu dữ liệu (dtype): {scores.dtype}")

# 2. Tính điểm tổng kết
weights = np.array([0.1, 0.2, 0.3, 0.4])
final_score = scores @ weights
print("\n2. Điểm tổng kết của 10 sinh viên:\n", np.round(final_score, 2))

# 3. Xếp loại sinh viên
conditions = [
    (final_score >= 8.5),
    (final_score >= 7.0) & (final_score < 8.5),
    (final_score >= 5.0) & (final_score < 7.0),
    (final_score < 5.0)
]
choices = ['A', 'B', 'C', 'D']
grades = np.select(conditions, choices, default='Unknown')
print("\n3. Xếp loại sinh viên:\n", grades)

# 4. Tìm sinh viên cao nhất, thấp nhất
print("\n4. Thống kê cực trị:")
print(f"- Điểm cao nhất: {np.max(final_score):.2f} (Sinh viên thứ {np.argmax(final_score) + 1})")
print(f"- Điểm thấp nhất: {np.min(final_score):.2f} (Sinh viên thứ {np.argmin(final_score) + 1})")

# 5. Lọc sinh viên >= 7.0
good_students = final_score[final_score >= 7.0]
print("\n5. Các điểm tổng kết từ 7.0 trở lên:\n", np.round(good_students, 2))

# 6. Phát hiện sinh viên có điểm thành phần < 5.0
low_component_idx = np.where(np.any(scores < 5.0, axis=1))[0]
print("\n6. Sinh viên có điểm thành phần < 5.0 (vị trí index):\n", low_component_idx)

# 7. Top 3 sinh viên
rank_idx = np.argsort(final_score)[::-1]
top3_idx = rank_idx[:3]
print("\n7. Top 3 sinh viên xuất sắc nhất (vị trí index):\n", top3_idx)
print("- Với các điểm số tương ứng:\n", np.round(final_score[top3_idx], 2))

# 8. Chuẩn hóa Z-score cột cuối kỳ
final_exam = scores[:, 3]
z_final_exam = (final_exam - final_exam.mean()) / final_exam.std()
print("\n8. Điểm cuối kỳ chuẩn hóa (Z-score):\n", np.round(z_final_exam, 2))

print("\n=> NHẬN XÉT BÀI 1:")
print("Phần lớn sinh viên đạt điểm Khá - Giỏi (>=7.0), chỉ có 1 sinh viên rơi vào nhóm có điểm thành phần dưới 5. Điểm Z-score cho thấy không có sinh viên nào có điểm cuối kỳ lệch quá xa (vượt mức 2 độ lệch chuẩn) so với trung bình lớp, chứng tỏ đề thi cuối kỳ có độ khó đồng đều.")
print("-" * 50)
import numpy as np

print("--- BÀI 2: PHÂN TÍCH CHUYÊN CẦN VÀ CẢNH BÁO HỌC VỤ ---")

# Ma trận chuyên cần (12 sinh viên, 8 buổi học)
attendance = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1]
])

# 1. Tổng số buổi đi học của từng sinh viên (axis=1 là theo hàng ngang)
present_count = attendance.sum(axis=1)
print("1. Tổng số buổi đi học của từng sinh viên:\n", present_count)

# 2. Tỉ lệ chuyên cần (%)
rate = present_count / attendance.shape[1] * 100
print("\n2. Tỉ lệ chuyên cần của từng sinh viên (%):\n", np.round(rate, 2))

# 3. Sinh viên bị cảnh báo (tỉ lệ < 75%)
warning_idx = np.where(rate < 75)[0]
print("\n3. Các sinh viên bị cảnh báo học vụ (index):\n", warning_idx)

# 4. Buổi học có số lượng vắng nhiều nhất
# Lọc các vị trí bằng 0, đếm theo cột dọc (axis=0)
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session)
print(f"\n4. Buổi học vắng nhiều nhất là buổi thứ {worst_session + 1} (với {absent_count_by_session[worst_session]} người vắng).")

# 5. Sinh viên đi học đầy đủ 8 buổi (tất cả các cột đều là 1)
full_attendance = np.where(np.all(attendance == 1, axis=1))[0]
print("\n5. Các sinh viên đi học đầy đủ 100% (index):\n", full_attendance)

# 6. Sinh viên có >= 2 buổi vắng liên tiếp
two_absent_in_row = np.where(np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1))[0]
print("\n6. Sinh viên có >= 2 buổi vắng liên tiếp (index):\n", two_absent_in_row)

# 7. Nhận xét ngắn
print("\n=> NHẬN XÉT BÀI 2:")
print("Ý thức học tập của lớp khá đáng báo động. Có nhiều sinh viên bị cảnh báo học vụ do nghỉ quá 25% số buổi (tỉ lệ < 75%). Đặc biệt, tình trạng nghỉ liên tiếp 2 buổi cũng xuất hiện ở nhiều cá nhân, và lớp chỉ có duy nhất 1 sinh viên duy trì được việc đi học đầy đủ tất cả các buổi.")
print("-" * 50)
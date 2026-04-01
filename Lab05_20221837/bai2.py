import numpy as np

print("--- BÀI 2: CHUẨN HÓA DỮ LIỆU BẰNG BROADCASTING ---")

# Sử dụng lại ma trận scores từ Bài 1
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# 1. Tính vector trung bình từng môn [cite: 349, 355]
mean_col = np.mean(scores, axis=0)
print("1. Vector trung bình từng môn:\n", mean_col)

# 2. Tính vector độ lệch chuẩn từng môn [cite: 350, 356]
std_col = np.std(scores, axis=0)
print("\n2. Vector độ lệch chuẩn từng môn:\n", np.round(std_col, 2))

# 3. Chuẩn hóa toàn bộ ma trận bằng Broadcasting (Z-score) [cite: 351, 357]
z_scores = (scores - mean_col) / std_col

# 4. In ma trận đã chuẩn hóa, làm tròn 2 chữ số thập phân [cite: 352, 358]
print("\n3 & 4. Ma trận Z-score (làm tròn 2 chữ số):\n", np.round(z_scores, 2))

# 5. Kiểm tra lại trung bình các cột sau chuẩn hóa 
# Kết quả hiển thị sẽ sát mức 0 [cite: 359]
print("\n5. TB các cột sau chuẩn hóa Z-score:\n", np.round(np.mean(z_scores, axis=0), 2))

# --- YÊU CẦU MỞ RỘNG ---
# Chuẩn hóa dữ liệu về khoảng [0, 1] theo từng môn 
print("\n--- YÊU CẦU MỞ RỘNG: CHUẨN HÓA MIN-MAX ---")
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)

# Công thức Min-Max Scaling
min_max_scores = (scores - min_col) / (max_col - min_col)

print("Ma trận chuẩn hóa Min-Max [0, 1] theo từng môn:\n", np.round(min_max_scores, 2))
print("-" * 50)
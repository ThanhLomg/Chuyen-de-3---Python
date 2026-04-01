import numpy as np
import matplotlib.pyplot as plt

print("--- BÀI 5: MÔ PHỎNG RANDOM WALK ---")

# Đặt seed để cố định kết quả ngẫu nhiên
np.random.seed(42)

# ==========================================
# PHẦN 1: MÔ PHỎNG 1 RANDOM WALK (100 BƯỚC)
# ==========================================
print("\n--- PHẦN 1: 1 RANDOM WALK ---")
# Tạo 100 bước ngẫu nhiên (chỉ có -1 hoặc 1)
steps = np.random.choice([-1, 1], size=100)

# Tính vị trí sau mỗi bước bằng hàm cộng dồn cumsum
walk = np.cumsum(steps)

print("1. Mười vị trí đầu tiên:", walk[:10])
print(f"2. Vị trí cuối cùng (bước 100): {walk[-1]}")
print(f"3. Vị trí lớn nhất đạt được: {np.max(walk)}")
print(f"4. Vị trí nhỏ nhất đạt được: {np.min(walk)}")

# Vẽ đồ thị Random Walk 1 chiều
plt.figure(figsize=(10, 5))
plt.plot(walk, label="Vị trí", color="blue")
plt.title("Random Walk 1 chiều (100 bước)")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.legend()
plt.show()

# ==========================================
# PHẦN 2: YÊU CẦU NÂNG CAO (100 RANDOM WALKS)
# ==========================================
print("\n--- PHẦN 2: 100 RANDOM WALKS ---")
# Tạo ma trận 100x100 (100 quá trình, mỗi quá trình 100 bước)
steps_many = np.random.choice([-1, 1], size=(100, 100))

# Tính vị trí cộng dồn theo từng hàng (axis=1)
walks_many = np.cumsum(steps_many, axis=1)

# Lấy cột cuối cùng để biết vị trí kết thúc của cả 100 quá trình
final_positions = walks_many[:, -1]

# Đếm số walk kết thúc ở vị trí dương (>0)
so_walk_duong = np.sum(final_positions > 0)
print(f"Số walk kết thúc ở vị trí dương: {so_walk_duong}")

# Đếm số walk chạm ngưỡng |10| (tức là >= 10 hoặc <= -10)
hit_10 = np.any(np.abs(walks_many) >= 10, axis=1)
print(f"Số walk chạm ngưỡng |10| trong quá trình di chuyển: {np.sum(hit_10)}")
print("-" * 50)
import numpy as np

print("--- BÀI 4: ĐẠI SỐ TUYẾN TÍNH CƠ BẢN VỚI NUMPY ---")

# Khởi tạo ma trận
A = np.array([
    [2, 1],
    [1, 3]
])
B = np.array([
    [4, 2],
    [1, 5]
])

# 1, 2, 3. Các phép toán cơ bản trên ma trận
print("1. A + B =\n", A + B)
print("\n2. A - B =\n", A - B)
print("\n3. Tích ma trận A @ B =\n", A @ B)

# 4. Tính định thức của A
det_A = np.linalg.det(A)
print("\n4. Định thức det(A) =", np.round(det_A, 2))

# 5. Tính ma trận nghịch đảo của A
inv_A = np.linalg.inv(A)
print("\n5. Ma trận nghịch đảo A^-1 =\n", np.round(inv_A, 2))

# 6. Giải hệ phương trình: 2x + y = 5 và x + 3y = 7
b = np.array([5, 7])
solution = np.linalg.solve(A, b)
print("\n6. Nghiệm của hệ phương trình (x, y):", np.round(solution, 2))

# --- YÊU CẦU MỞ RỘNG ---
print("\n--- YÊU CẦU MỞ RỘNG ---")
# Hàm allclose kiểm tra xem 2 mảng có bằng nhau (hoặc xấp xỉ bằng nhau) không
kiem_tra = np.allclose(A @ solution, b)
print(f"Kiểm tra lại nghiệm (A @ nghiệm == b): {kiem_tra}")
print("Giải thích: Một ma trận sẽ KHÔNG khả nghịch (không thể tìm được ma trận nghịch đảo) khi định thức của nó det(A) = 0.")
print("-" * 50)
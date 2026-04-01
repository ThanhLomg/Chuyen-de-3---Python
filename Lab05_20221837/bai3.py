import numpy as np

print("--- BÀI 3: PHÂN TÍCH DOANH THU BẰNG PHÉP TOÁN MA TRẬN ---")

# Khởi tạo dữ liệu
quantity = np.array([
    [10, 12, 9, 14],
    [5, 7, 8, 6],
    [20, 18, 25, 22]
])
price = np.array([15000, 25000, 10000])

# 1. Tính doanh thu của từng sản phẩm theo từng ngày (Broadcasting)
revenue = quantity * price.reshape(3, 1)
print("1. Doanh thu từng sản phẩm theo ngày:\n", revenue)

# 2. Tính tổng doanh thu của từng sản phẩm (tính theo hàng: axis=1)
sum_product = np.sum(revenue, axis=1)
print("\n2. Tổng doanh thu từng sản phẩm:\n", sum_product)

# 3. Tính tổng doanh thu của từng ngày (tính theo cột: axis=0)
sum_day = np.sum(revenue, axis=0)
print("\n3. Tổng doanh thu từng ngày:\n", sum_day)

# 4. Tìm ngày có doanh thu cao nhất
best_day = np.argmax(sum_day) + 1
print(f"\n4. Ngày doanh thu cao nhất: Ngày {best_day}")

# 5. Tính tỷ trọng doanh thu của từng sản phẩm
ratio = sum_product / np.sum(sum_product)
print("\n5. Tỷ trọng doanh thu từng sản phẩm (%):\n", np.round(ratio * 100, 2))
print("-" * 50)
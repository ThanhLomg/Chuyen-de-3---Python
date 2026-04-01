import numpy as np

print("--- BÀI 3: PHÂN TÍCH DOANH THU BÁN HÀNG (KINH DOANH) ---")

# Ma trận doanh thu (7 ngày, 5 sản phẩm)
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

# 1. Tổng doanh thu theo từng ngày (tính theo hàng: axis=1)
daily_total = sales.sum(axis=1)
print("1. Tổng doanh thu từng ngày trong tuần:\n", daily_total)

# 2. Tổng doanh thu và doanh thu trung bình của từng sản phẩm (tính theo cột: axis=0)
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)
print("\n2. Tổng doanh thu từng sản phẩm:\n", product_total)
print("   Doanh thu trung bình từng sản phẩm:\n", np.round(product_mean, 2))

# 3. Ngày doanh thu cao nhất và sản phẩm bán tốt nhất
best_day = np.argmax(daily_total)
best_product = np.argmax(product_total)
print(f"\n3. Ngày có doanh thu cao nhất: Ngày thứ {best_day + 1} (Doanh thu: {daily_total[best_day]})")
print(f"   Sản phẩm bán tốt nhất: Sản phẩm thứ {best_product + 1} (Tổng thu: {product_total[best_product]})")

# 4. Điều chỉnh tăng 8% cho sản phẩm 2 và 5 (tức là cột index 1 và 4)
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08
print("\n4. Doanh thu sau khi tăng 8% cho SP 2 và SP 5:\n", np.round(new_sales, 2))

# 5. So sánh tổng doanh thu trước và sau điều chỉnh
before_total = sales.sum()
after_total = new_sales.sum()
print(f"\n5. Tổng doanh thu TRƯỚC điều chỉnh: {before_total}")
print(f"   Tổng doanh thu SAU điều chỉnh: {after_total:.2f}")

# 6. Các ngày có doanh thu > trung bình toàn tuần
high_days = np.where(daily_total > daily_total.mean())[0]
print(f"\n6. Các ngày có doanh thu vượt mức trung bình tuần: Ngày {high_days + 1}")

# 7. Sản phẩm ổn định nhất (độ lệch chuẩn nhỏ nhất)
stable_product = np.argmin(sales.std(axis=0))
print(f"\n7. Sản phẩm ổn định nhất: Sản phẩm thứ {stable_product + 1} (Độ lệch chuẩn nhỏ nhất)")

# 8. Nhận xét
print("\n=> NHẬN XÉT BÀI 3:")
print(f"Sản phẩm thứ {best_product + 1} là mặt hàng mang lại doanh thu chủ lực, cửa hàng cần ưu tiên nhập số lượng lớn. Ngoài ra, sản phẩm thứ {stable_product + 1} có mức tiêu thụ cực kỳ ổn định, là mặt hàng thiết yếu giúp duy trì nguồn thu đều đặn mỗi ngày.")
print("-" * 50)
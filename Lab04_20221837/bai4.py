import numpy as np

print("--- BÀI 4: QUẢN LÝ TỒN KHO VÀ ĐỀ XUẤT NHẬP HÀNG ---")

# Dữ liệu đầu vào
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

# 1 & 2. Số lượng cần nhập thêm cho từng mặt hàng
# (Chỉ nhập khi stock < min_stock, nếu thừa thì thay bằng 0)
need_import = np.maximum(min_stock - stock, 0)
print("1 & 2. Số lượng cần nhập thêm cho từng mặt hàng:\n", need_import)

# 3. Chi phí nhập thêm cho từng mặt hàng
cost = need_import * price
print("\n3. Chi phí nhập thêm cho từng mặt hàng:\n", cost)

# 4. Tính tổng chi phí nhập hàng
total_cost = cost.sum()
print(f"\n4. Tổng chi phí nhập hàng dự kiến: {total_cost}")

# 5. Phân loại trạng thái "Thiếu hàng" hoặc "Đủ hàng"
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
print("\n5. Trạng thái của từng mặt hàng:\n", status)

# 6. Tìm 3 mặt hàng thiếu nhiều nhất
# argsort sắp xếp tăng dần, [::-1] lật ngược lại thành giảm dần
top3_shortage_idx = np.argsort(need_import)[::-1][:3]
print("\n6. Top 3 mặt hàng thiếu hụt nghiêm trọng nhất (vị trí index):", top3_shortage_idx)
print("   - Số lượng thiếu tương ứng:", need_import[top3_shortage_idx])

# 7. Giới hạn số lượng nhập tối đa mỗi mặt hàng là 20 đơn vị
limited_need = np.clip(need_import, 0, 20)
print("\n7. Số lượng nhập sau khi áp dụng giới hạn tối đa 20 đơn vị:\n", limited_need)

# 8. Tính lại tổng chi phí sau khi giới hạn
limited_total_cost = (limited_need * price).sum()
print(f"\n8. Tổng chi phí sau khi giới hạn lượng nhập: {limited_total_cost}")

# 9. Viết nhận xét ngắn
print("\n=> NHẬN XÉT BÀI 4:")
print("Kho hàng đang rơi vào tình trạng thiếu hụt ở nhiều mã sản phẩm (6/10 mặt hàng có trạng thái Thiếu hàng). Tuy nhiên, mức độ thiếu hụt của từng mặt hàng là không quá lớn (số lượng cần nhập lớn nhất chỉ là 7 đơn vị, hoàn toàn nằm dưới ngưỡng giới hạn 20). Do đó, tổng chi phí nhập hàng trước và sau khi chạy hàm np.clip không có sự thay đổi.")
print("-" * 50)
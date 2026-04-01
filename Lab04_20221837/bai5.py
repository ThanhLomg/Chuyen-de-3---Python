print("\n--- BÀI 5: TỔNG HỢP VÀ SO SÁNH HAI MIỀN LĨNH VỰC ---")
print("Lựa chọn: So sánh Bài 1 (Miền Giáo dục) và Bài 3 (Miền Kinh doanh)\n")

print("Câu 1. Dữ liệu ở hai bài giống nhau ở điểm nào về cấu trúc?")
print("=> Trả lời: Cả hai bài đều sử dụng mảng 2 chiều (2D ndarray) của NumPy để biểu diễn dữ liệu dạng bảng. Các hàng đại diện cho đối tượng (sinh viên, ngày bán), và các cột đại diện cho thuộc tính (đầu điểm, sản phẩm).")

print("\nCâu 2. Phép toán NumPy nào được dùng ở cả hai bài?")
print("=> Trả lời: Cả hai đều dùng các hàm tổng hợp dữ liệu (np.max, np.sum, np.mean, np.argmax) kết hợp với các thao tác trên trục (axis=0, axis=1).")

print("\nCâu 3. Bài nào sử dụng boolean indexing nhiều hơn? Vì sao?")
print("=> Trả lời: Miền Giáo dục (Bài 1, Bài 2) dùng nhiều hơn. Vì tính chất bài toán giáo dục thường xuyên phải lọc và phân loại dữ liệu theo các ngưỡng điều kiện chặt chẽ (ví dụ: điểm >= 7.0, chuyên cần < 75%).")

print("\nCâu 4. Lợi ích của xử lý vector hóa so với dùng vòng lặp là gì?")
print("=> Trả lời: Mã nguồn ngắn gọn, dễ bảo trì, loại bỏ hoàn toàn vòng lặp for thủ công. Tốc độ thực thi cực kỳ nhanh do NumPy gọi các thư viện C/C++ xử lý song song ở dưới nền.")

print("\nCâu 5. Nếu số lượng dữ liệu tăng gấp 100 lần, NumPy hỗ trợ gì cho việc xử lý?")
print("=> Trả lời: Nhờ cơ chế Broadcasting và tối ưu hóa lưu trữ bộ nhớ liên tục, độ phức tạp của code NumPy không thay đổi. Nó vẫn xử lý mảng dữ liệu khổng lồ cực nhanh mà không bị tràn RAM như cấu trúc List thông thường.")

print("\n" + "="*50)
print("CHÚC MỪNG! BẠN ĐÃ HOÀN THÀNH XUẤT SẮC TOÀN BỘ LAB 4!")
print("="*50)
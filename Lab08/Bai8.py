import pandas as pd

print("--- BÀI 8: GHI DỮ LIỆU RA CSV VÀ EXCEL ---")
try:
    # 1. Đọc dữ liệu từ file sales.csv 
    df_sales = pd.read_csv('sales.csv')
    
    # 2. Lọc ra các đơn hàng có doanh thu > 50000
    df_high_sales = df_sales[df_sales['DoanhThu'] > 50000]
    
    # 3. Ghi kết quả ra file mới
    df_high_sales.to_csv('high_sales.csv', index=False)
    df_high_sales.to_excel('high_sales.xlsx', index=False)
    
    print("Thành công! Đã lọc và xuất ra file 'high_sales.csv' và 'high_sales.xlsx'.")
    print("\nKết quả dữ liệu đã lọc:\n", df_high_sales)
    
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'sales.csv'. Bạn kiểm tra lại thư mục nhé!")
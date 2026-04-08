import os
import pandas as pd

print("\n--- BÀI NC 4: HÀM NẠP DỮ LIỆU TỔNG QUÁT ---")
def load_data(file_path):
    # Tách lấy phần đuôi mở rộng của file (vd: '.csv', '.xlsx')
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    try:
        if ext == '.csv': 
            return pd.read_csv(file_path, dtype={'MaKH': str}) # Ép kiểu phòng hờ
        elif ext in ['.xls', '.xlsx']: 
            return pd.read_excel(file_path)
        elif ext == '.json': 
            return pd.read_json(file_path)
        else:
            print(f"Lỗi: Định dạng {ext} không được hỗ trợ!")
            return None
    except Exception as e:
        print(f"Lỗi khi đọc file {file_path}: {e}")
        return None

# Gọi thử hàm với 2 định dạng khác nhau
print("Đọc CSV qua hàm:", load_data('students.csv').shape)
print("Đọc JSON qua hàm:", load_data('products.json').shape)
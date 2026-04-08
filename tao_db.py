import sqlite3

print("Đang tạo cơ sở dữ liệu shop.db và bảng orders...")

# Kết nối đến file shop.db (tự động tạo nếu chưa có)
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Tạo bảng 'orders' với các cột tương ứng
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        OrderID TEXT PRIMARY KEY,
        CustomerName TEXT,
        TotalAmount REAL,
        OrderDate TEXT
    )
''')

# Dữ liệu mẫu cần chèn vào bảng
dulieu_mau = [
    ('ORD001', 'Nguyen Van A', 1500000, '2026-04-01'),
    ('ORD002', 'Tran Thi B', 500000, '2026-04-02'),
    ('ORD003', 'Le Van C', 2500000, '2026-04-03'),
    ('ORD004', 'Pham Thi D', 800000, '2026-04-04')
]

# Chèn dữ liệu vào bảng (sử dụng INSERT OR IGNORE để chạy lại file không bị lỗi trùng khóa)
cursor.executemany('''
    INSERT OR IGNORE INTO orders (OrderID, CustomerName, TotalAmount, OrderDate)
    VALUES (?, ?, ?, ?)
''', dulieu_mau)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Thành công! Đã tạo xong file shop.db với bảng 'orders' và dữ liệu mẫu.")
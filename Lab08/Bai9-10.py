import sqlite3
import pandas as pd
print("\n--- BÀI 9 & 10 ---")
# Đọc JSON
df_json = pd.read_json('products.json')
print("Dữ liệu JSON:\n", df_json.head(2))

# Kết nối SQLite (Yêu cầu có file shop.db)
try:
    conn = sqlite3.connect('shop.db')
    df_sql = pd.read_sql('SELECT * FROM orders', conn)
    print("Tổng số đơn:", len(df_sql))
    print("Tổng doanh thu:", df_sql['TotalAmount'].sum())
    conn.close()
except sqlite3.OperationalError:
    print("Lưu ý: Không tìm thấy file shop.db để kiểm tra Bài 10.")
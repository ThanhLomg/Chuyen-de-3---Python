import pandas as pd
import json

def load_data(file_path):
    """Load data from CSV, Excel, or JSON files"""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return pd.DataFrame(json.load(f))
    return None

print("\n--- BÀI NC 5: MINI PROJECT ETL ĐƠN GIẢN ---")
# 1. EXTRACT (Nạp dữ liệu bằng hàm thông minh vừa viết ở Bài 4)
df_cus = load_data('customers.csv')
df_ord = load_data('orders.xlsx')
df_prod = load_data('products.json')

if all(df is not None for df in [df_cus, df_ord, df_prod]):
    # 2. TRANSFORM (Biến đổi dữ liệu)
    # Gộp 3 bảng lại với nhau (Đơn hàng + Khách hàng + Sản phẩm)
    df_merge1 = pd.merge(df_ord, df_cus, on='MaKH', how='inner')
    df_final = pd.merge(df_merge1, df_prod, on='MaSP', how='inner')
    
    # Tính báo cáo 1: Số đơn hàng theo từng khách hàng
    bc_kh = df_final.groupby('TenKH')['MaDH'].count().reset_index(name='SoDonHang')
    
    # Tính báo cáo 2: Tổng tiền theo nhóm sản phẩm
    df_final['ThanhTien'] = df_final['SoLuong'] * df_final['Gia']
    bc_sp = df_final.groupby('NhomHang')['ThanhTien'].sum().reset_index()
    
    # 3. LOAD (Ghi dữ liệu)
    # Lưu 2 bảng báo cáo vào 2 sheet khác nhau trong cùng 1 file Excel
    with pd.ExcelWriter('BaoCao_ETL.xlsx') as writer:
        bc_kh.to_excel(writer, sheet_name='BaoCaoKhachHang', index=False)
        bc_sp.to_excel(writer, sheet_name='BaoCaoSanPham', index=False)
        
    print("=> QUÁ TRÌNH ETL HOÀN TẤT! Đã xuất file 'BaoCao_ETL.xlsx' gồm 2 sheet.")
import pandas as pd

print("Đang tạo file inventory.xlsx...")

# 1. Dữ liệu sheet HangHoa (Cố tình để một số mặt hàng tồn < 20 để test Bài 6)
data_hanghoa = {
    'MaSP': ['SP01', 'SP02', 'SP03', 'SP04', 'SP05'],
    'TenSP': ['Bàn phím cơ', 'Chuột không dây', 'Màn hình 24 inch', 'Tai nghe Bluetooth', 'Lót chuột'],
    'SoLuongTon': [15, 50, 8, 35, 12],
    'GiaBan': [850000, 300000, 2500000, 450000, 50000]
}

# 2. Dữ liệu sheet NhapKho (Phục vụ Bài 7)
data_nhapkho = {
    'MaPhieu': ['PN01', 'PN02'],
    'NgayNhap': ['2026-04-01', '2026-04-02'],
    'MaSP': ['SP01', 'SP03'],
    'SoLuong': [50, 20]
}

# 3. Dữ liệu sheet XuatKho (Phục vụ Bài 7)
data_xuatkho = {
    'MaPhieu': ['PX01', 'PX02'],
    'NgayXuat': ['2026-04-03', '2026-04-05'],
    'MaSP': ['SP02', 'SP04'],
    'SoLuong': [10, 5]
}

# Sử dụng ExcelWriter để ghi nhiều sheet vào cùng 1 file
with pd.ExcelWriter('inventory.xlsx') as writer:
    pd.DataFrame(data_hanghoa).to_excel(writer, sheet_name='HangHoa', index=False)
    pd.DataFrame(data_nhapkho).to_excel(writer, sheet_name='NhapKho', index=False)
    pd.DataFrame(data_xuatkho).to_excel(writer, sheet_name='XuatKho', index=False)

print("Thành công! File 'inventory.xlsx' đã xuất hiện trong thư mục của bạn.")
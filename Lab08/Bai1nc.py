import pandas as pd

print("--- BÀI NC 1: TÍCH HỢP CSV VÀ EXCEL ---")
# Nạp dữ liệu
df_students = pd.read_csv('students.csv')
df_scores = pd.read_excel('scores.xlsx')

# Ghép 2 bảng (tương tự hàm VLOOKUP trong Excel)
df_tonghop = pd.merge(df_students, df_scores, on='MaSV', how='inner')

# Tính thêm điểm tổng kết (Giả sử QT 40%, Thi 60%)
df_tonghop['DiemTongKet'] = 0.4 * df_tonghop['DiemQT'] + 0.6 * df_tonghop['DiemThi']

# Lưu ra file Excel mới
df_tonghop.to_excel('tonghop_diem.xlsx', index=False)
print("Kết quả Bảng tổng hợp điểm:\n", df_tonghop)
print("=> Đã lưu thành công file 'tonghop_diem.xlsx'")
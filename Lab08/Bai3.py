import pandas as pd

print("\n--- BÀI 3 ---")
ten_cot = ['MaSV', 'HoTen', 'Lop', 'DiemQT', 'DiemThi']
df_scores = pd.read_csv('scores_no_header.csv', header=None, names=ten_cot)
df_scores.info() # Hiển thị thông tin dữ liệu
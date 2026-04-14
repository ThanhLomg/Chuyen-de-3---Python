import pandas as pd
import numpy as np

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# 1. Kiểm tra các giá trị điểm không hợp lệ (ngoài khoảng 0–10)
invalid_score = ~df["score_python"].between(0, 10)

print("Các dòng có điểm sai:")
print(df.loc[invalid_score, ["student_id", "score_python"]])

# 2. Gán các giá trị sai thành NaN
df.loc[invalid_score, "score_python"] = np.nan

# 3. Thay NaN bằng giá trị trung vị (median)
df["score_python"] = df["score_python"].fillna(
    df["score_python"].median()
)

# 4. Kiểm tra lại
print("\nSau khi xử lý:")
print(df["score_python"].describe())

# 5. Xem kết quả
print(df[["student_id", "score_python"]])
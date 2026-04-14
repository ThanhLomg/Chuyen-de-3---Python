import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# kiểm tra giá trị thiếu
print("Số giá trị thiếu ban đầu:")
print(df.isna().sum())

# 1. Xử lý cột gender
df["gender"] = df["gender"].fillna("Không rõ")

# 2. Xử lý cột attendance_rate (điểm danh)
df["attendance_rate"] = df["attendance_rate"].fillna(
    df["attendance_rate"].median()
)

# 3. Xử lý cột phone
df["phone"] = df["phone"].fillna("Chưa cập nhật")

# kiểm tra lại
print("\nSau khi xử lý:")
print(df.isna().sum())

# xem kết quả
print(df.head())
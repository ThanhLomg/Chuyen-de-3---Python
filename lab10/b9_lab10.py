import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# 1. Tính Q1, Q3
Q1 = df["attendance_rate"].quantile(0.25)
Q3 = df["attendance_rate"].quantile(0.75)

# 2. Tính IQR
IQR = Q3 - Q1

# 3. Xác định ngưỡng
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Ngưỡng dưới:", lower_bound)
print("Ngưỡng trên:", upper_bound)

# 4. Lọc outlier
outliers = df[
    (df["attendance_rate"] < lower_bound) |
    (df["attendance_rate"] > upper_bound)
]

# 5. Hiển thị kết quả
print("\nCác giá trị ngoại lệ:")
print(outliers[["student_id", "attendance_rate"]])
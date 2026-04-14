import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# 1. Kiểm tra số dòng trùng hoàn toàn
print("Số dòng trùng hoàn toàn:", df.duplicated().sum())

# 2. Kiểm tra trùng theo student_id
print("Số student_id trùng:", df.duplicated(subset=["student_id"]).sum())

# 3. Hiển thị các dòng trùng (nếu muốn xem)
print("\nDòng trùng hoàn toàn:")
print(df[df.duplicated()])

print("\nDòng trùng theo student_id:")
print(df[df.duplicated(subset=["student_id"], keep=False)])

# 4. Xóa dòng trùng hoàn toàn
df = df.drop_duplicates()

# 5. Xóa trùng theo student_id (giữ dòng đầu)
df = df.drop_duplicates(subset=["student_id"], keep="first")

# 6. Kiểm tra lại
print("\nSau khi xóa:")
print("Số dòng còn lại:", len(df))
print("Còn trùng student_id không:", df.duplicated(subset=["student_id"]).sum())

# 7. Hiển thị kết quả
print(df.head())
import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# 1. Chuyển cột birth_date sang kiểu datetime
df["birth_date"] = pd.to_datetime(
    df["birth_date"],
    errors="coerce",   # giá trị sai sẽ thành NaT
    dayfirst=True      # ưu tiên định dạng ngày/tháng/năm
)

# 2. Kiểm tra giá trị lỗi
print("Số giá trị ngày lỗi:", df["birth_date"].isna().sum())

print("\nCác dòng bị lỗi ngày:")
print(df[df["birth_date"].isna()][["student_id", "birth_date"]])

# 3. Xem kết quả sau khi chuyển
print("\nDữ liệu sau khi chuẩn hóa:")
print(df[["student_id", "birth_date"]].head())
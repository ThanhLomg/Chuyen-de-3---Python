import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# 1. Chuẩn hóa full_name
df["full_name"] = (
    df["full_name"]
    .str.replace(r"\s+", " ", regex=True)   # xóa khoảng trắng dư
    .str.strip()                            # xóa khoảng trắng đầu/cuối
    .str.title()                            # viết hoa chữ cái đầu
)

# 2. Kiểm tra email hợp lệ
email_valid = df["email"].str.contains(
    r"^[\w\.-]+@[\w\.-]+\.\w+$",
    regex=True,
    na=False
)

print("Email không hợp lệ:")
print(df.loc[~email_valid, ["student_id", "email"]])

# 3. Chuẩn hóa phone (chỉ giữ số)
df["phone"] = (
    df["phone"]
    .astype("string")
    .str.replace(r"\D", "", regex=True)   # xóa tất cả ký tự không phải số
)

# xem kết quả
print(df[["full_name", "email", "phone"]])
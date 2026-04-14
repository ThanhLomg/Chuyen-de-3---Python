import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# (giả sử bạn đã xử lý các bước từ bài 1 → 9)

# 1. Lưu file mới
df.to_csv(
    "Chuyen-de-3---Python/lab10/student_performance_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Đã lưu file sạch thành công!")

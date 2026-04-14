import pandas as pd

# đọc file
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# 1. Tạo khoảng điểm
bins = [0, 5, 6.5, 8, 10]

# 2. Gán nhãn học lực
labels = ["Yếu", "Trung bình", "Khá", "Giỏi"]

# 3. Phân loại
df["level"] = pd.cut(
    df["score_python"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# 4. Xem kết quả
print(df[["student_id", "score_python", "level"]])
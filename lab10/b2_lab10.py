import pandas as pd

# đọc file đúng
df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv")

# kiểm tra cột
print("Tên cột:", df.columns)

# chuẩn hóa tên cột
df.columns = df.columns.str.strip()

# chuẩn hóa class_name
df["class_name"] = (
    df["class_name"]
    .str.replace("-", " ", regex=False)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
    .str.upper()
    .replace({
        "CNTT1": "CNTT 1",
        "CNTT2": "CNTT 2",
        "CNTT3": "CNTT 3"
    })
)

# chuẩn hóa gender
df["gender"] = (
    df["gender"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({
        "nam": "Nam",
        "nữ": "Nữ",
        "nu": "Nữ"
    })
)

# kết quả
print(df[["class_name", "gender"]])
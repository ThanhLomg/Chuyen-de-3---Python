import pandas as pd
import numpy as np

print("Đang tạo file dữ liệu mẫu data.csv cho Lab 11...")
np.random.seed(42)
n_samples = 200

# Tạo dữ liệu giả lập
data = {
    "Nhom": np.random.choice(["A", "B", "C"], size=n_samples),
    "GiaTri": np.random.normal(loc=50, scale=15, size=n_samples), # Phân phối chuẩn
    "X": np.random.uniform(0, 10, size=n_samples),
    "X1": np.random.uniform(0, 10, size=n_samples),
    "X2": np.random.uniform(0, 10, size=n_samples),
}

df = pd.DataFrame(data)
# Tạo biến Y phụ thuộc tuyến tính vào X (Cho Bài 6)
df["Y"] = 3.5 * df["X"] + 10 + np.random.normal(0, 3, size=n_samples)

# Tạo biến Label (0 hoặc 1) phụ thuộc vào X1 và X2 (Cho Bài 7)
df["Label"] = np.where(df["X1"] + df["X2"] > 10, 1, 0)

df.to_csv("data.csv", index=False)
print("Thành công! Đã tạo xong file data.csv.")
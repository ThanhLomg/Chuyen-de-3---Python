import pandas as pd
import matplotlib.pyplot as plt

# Đọc file
df = pd.read_csv("lab9/moitruong.csv")

# 1. Tính IQR
Q1 = df['NhietDo'].quantile(0.25)
Q3 = df['NhietDo'].quantile(0.75)
IQR = Q3 - Q1

# 2. Xác định outlier
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['Outlier'] = (df['NhietDo'] < lower) | (df['NhietDo'] > upper)

print("📌 Các giá trị ngoại lệ:")
print(df[df['Outlier']])

# 3. Thay outlier bằng median
median = df['NhietDo'].median()
df.loc[df['Outlier'], 'NhietDo'] = median

# 4. Thống kê
print("📊 Sau khi xử lý:")
print(df.describe())

# 5. Vẽ boxplot
plt.boxplot(df['NhietDo'])
plt.title("Boxplot NhietDo")
plt.show()

# Lưu file
df.to_csv("lab9/clean_bai9.csv", index=False)

print("✅ Đã xử lý xong bài 9")
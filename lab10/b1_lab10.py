import pandas as pd

df = pd.read_csv("Chuyen-de-3---Python/lab10/student_performance_dirty.csv", on_bad_lines='skip')

print("5 dòng đầu:")
print(df.head())

print("\nThông tin dữ liệu:")
print(df.info())
print("\nSố giá trị thiếu:")
print(df.isna().sum())
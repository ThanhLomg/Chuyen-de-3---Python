import pandas as pd
import numpy as np

df = pd.read_csv("Lab07_20221837/diem_sinhvien.csv")

print("=== 5 dòng đầu ===")
print(df.head())

print("\n=== 5 dòng cuối ===")
print(df.tail())

print("\n=== Thông tin dữ liệu ===")
print(df.info())

print("\n=== Thống kê mô tả ===")
print(df.describe())
import pandas as pd
import sqlite3

print("--- BÀI 1 ---")
df_students = pd.read_csv('students.csv')
print(df_students.head()) # Hiển thị 5 dòng đầu
print(f"Kích thước: {df_students.shape[0]} dòng, {df_students.shape[1]} cột") # Dùng attribute shape
print("Tên cột:", df_students.columns.tolist())
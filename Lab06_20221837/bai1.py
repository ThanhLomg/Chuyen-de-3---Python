import pandas as pd

print("--- BÀI 1: LÀM QUEN VỚI SERIES ---")
# Tạo Series với chỉ mục là mã sinh viên
diem = pd.Series(
    [7.5, 8.0, 6.5, 9.0, 8.5],
    index=["SV01", "SV02", "SV03", "SV04", "SV05"]
)

print("1. Toàn bộ danh sách điểm:")
print(diem)

print("\n2. Hai phần tử đầu tiên:")
print(diem.head(2))

print(f"\n3. Điểm lớn nhất: {diem.max()}")
print(f"4. Điểm trung bình: {diem.mean()}")

print("\n5. Sinh viên có điểm >= 8:")
print(diem[diem >= 8])
print("-" * 50)
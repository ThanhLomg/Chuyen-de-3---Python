import pandas as pd

print("--- BÀI 5: ỨNG DỤNG TRONG NGHIÊN CỨU KHOA HỌC ---")
# Tạo dữ liệu khảo sát
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}
df = pd.DataFrame(data)

# Tính cột điểm trung bình
df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

# Hàm phân nhóm học tập
def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    else:
        return "Can ho tro"

# Dùng apply với axis=1 để áp dụng trên từng hàng ngang
df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

print("1. Toàn bộ dữ liệu sau khi phân nhóm học tập:")
print(df)

print("\n2. Sinh viên tự học > 2 giờ và nghỉ <= 2 buổi:")
print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])

print("\n=> NHẬN XÉT: Qua dữ liệu, ta thấy nhóm sinh viên có thời gian tự học cao (>=3h) và ít nghỉ học thường đạt điểm tổng kết rất tốt và rơi vào nhóm 'Tích cực'. Ngược lại, những sinh viên nghỉ học nhiều và lười tự học đều bị xếp vào nhóm 'Cần hỗ trợ' với điểm số rất thấp. Điều này cho thấy mối tương quan đồng biến mạnh mẽ giữa sự chuyên cần và kết quả học tập.")
print("-" * 50)
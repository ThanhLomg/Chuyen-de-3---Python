print("\n--- BÀI 5: KIỂM TRA ĐẦU VÀO ---")
# Yêu cầu nhập điểm từ 0 đến 10
diem_nhap = float(input("Nhập điểm từ 0 đến 10: "))

while diem_nhap < 0 or diem_nhap > 10:
    print("Dữ liệu không hợp lệ, vui lòng nhập lại.")
    diem_nhap = float(input("Nhập điểm từ 0 đến 10: "))

    print("Điểm hợp lệ là:", diem_nhap)
import requests
import pandas as pd

print("\n--- BÀI NC 3: ĐỌC DỮ LIỆU TỪ WEB API ---")
url = "https://jsonplaceholder.typicode.com/users" # API mẫu miễn phí

# Gửi request lên server để lấy dữ liệu
response = requests.get(url)

if response.status_code == 200: # 200 nghĩa là lấy thành công
    # Chuyển đổi JSON nhận được thành DataFrame
    df_api = pd.DataFrame(response.json())
    
    # Lọc ra 4 cột quan trọng nhất
    df_api_clean = df_api[['id', 'name', 'email', 'phone']]
    
    # Lưu lại
    df_api_clean.to_csv('api_users.csv', index=False)
    print("Dữ liệu lấy từ API:\n", df_api_clean.head(3))
    print("=> Đã lưu thành công file 'api_users.csv'")
else:
    print("Lỗi không lấy được dữ liệu từ API!")
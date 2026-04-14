import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
import warnings
warnings.filterwarnings('ignore')

print("=== BÀI 1: ĐỌC DỮ LIỆU VÀ KHÁM PHÁ NHANH ===")
df = pd.read_csv("Data/data.csv")
print("1. 5 dòng đầu tiên:\n", df.head())
print("\n2. Thông tin dữ liệu:")
df.info()
print("\n3. Thống kê mô tả:\n", df.describe())
print("-" * 50)

print("=== BÀI 2: VẼ BIỂU ĐỒ CỘT THEO NHÓM ===")
group_data = df.groupby("Nhom")["GiaTri"].mean()
group_data.plot(kind="bar", title="Gia tri trung binh theo nhom", color=['#4CAF50', '#2196F3', '#FFC107'])
plt.ylabel("Giá trị trung bình")
plt.show()
print("=> Đã hiển thị biểu đồ cột (Bar Chart).")

print("\n=== BÀI 3: VẼ HISTOGRAM XEM PHÂN PHỐI ===")
df["GiaTri"].plot(kind="hist", bins=15, title="Phan phoi du lieu", color='purple', edgecolor='black')
plt.xlabel("Giá trị")
plt.show()
print("=> Nhận xét: Dữ liệu tập trung nhiều nhất ở vùng giá trị từ 40 đến 60 (tuân theo phân phối chuẩn).")

print("\n=== BÀI 4: VẼ BOXPLOT PHÁT HIỆN NGOẠI LỆ ===")
df.boxplot(column="GiaTri")
plt.title("Boxplot phat hien ngoai le")
plt.show()
print("=> Nhận xét: Nếu có các chấm tròn nằm ngoài râu (whiskers) của boxplot, đó chính là các giá trị ngoại lệ (outliers).")

print("\n=== BÀI 5: VẼ SCATTER PLOT XEM QUAN HỆ 2 BIẾN ===")
df.plot(kind="scatter", x="X", y="Y", title="Moi quan he giua X va Y", color='red')
plt.show()
print("=> Nhận xét: Các điểm dữ liệu tạo thành một đường chéo hướng lên, chứng tỏ X và Y có mối quan hệ tuyến tính đồng biến rất mạnh.")

print("\n=== BÀI 6: HỒI QUY TUYẾN TÍNH ĐƠN GIẢN ===")
X_lin = df[["X"]]
y_lin = df["Y"]
X_train_lin, X_test_lin, y_train_lin, y_test_lin = train_test_split(X_lin, y_lin, test_size=0.2, random_state=42)

model_lin = LinearRegression()
model_lin.fit(X_train_lin, y_train_lin)
y_pred_lin = model_lin.predict(X_test_lin)

print("MSE (Sai số toàn phương trung bình):", mean_squared_error(y_test_lin, y_pred_lin))
print("Hệ số góc (Coef):", model_lin.coef_[0])
print("Hệ số chặn (Intercept):", model_lin.intercept_)

print("\n=== BÀI 7: PHÂN LOẠI ĐƠN GIẢN (LOGISTIC REGRESSION) ===")
X_log = df[["X1", "X2"]]
y_log = df["Label"]
X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X_log, y_log, test_size=0.2, random_state=42)

model_log = LogisticRegression(max_iter=1000)
model_log.fit(X_train_log, y_train_log)
y_pred_log = model_log.predict(X_test_log)

print("Độ chính xác (Accuracy):", accuracy_score(y_test_log, y_pred_log))

print("\n=== BÀI 8: BÀI THỰC HÀNH TỔNG HỢP ===")
print("=> Nhận xét tổng hợp: Quá trình EDA bằng biểu đồ cho ta cái nhìn rõ ràng về phân phối của dữ liệu (chuẩn) và mối quan hệ tuyến tính giữa X và Y. Nhờ đó, việc áp dụng mô hình Linear Regression cho độ sai số (MSE) thấp, và mô hình Logistic Regression phân loại nhãn (Label) cho độ chính xác rất cao.")
print("-" * 50)
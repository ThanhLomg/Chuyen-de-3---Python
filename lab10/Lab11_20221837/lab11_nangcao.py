import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

print("=== ĐỌC DỮ LIỆU CHUẨN BỊ CHO PHẦN NÂNG CAO ===")
df = pd.read_csv("Data/data.csv")
print("Đã nạp dữ liệu thành công!\n")

print("=== BÀI NC 1 & 4: SO SÁNH MÔ HÌNH VÀ SỐ LƯỢNG BIẾN ===")
# Mô hình 1 biến (X)
X1_var = df[["X"]]
y_reg = df["Y"]
X_tr1, X_te1, y_tr1, y_te1 = train_test_split(X1_var, y_reg, test_size=0.2, random_state=42)

lr1 = LinearRegression()
lr1.fit(X_tr1, y_tr1)
pred_lr1 = lr1.predict(X_te1)

# Mô hình nhiều biến (X, X1, X2)
X_multi = df[["X", "X1", "X2"]]
X_tr_m, X_te_m, y_tr_m, y_te_m = train_test_split(X_multi, y_reg, test_size=0.2, random_state=42)

lr_multi = LinearRegression()
lr_multi.fit(X_tr_m, y_tr_m)
pred_lr_multi = lr_multi.predict(X_te_m)

# Mô hình Decision Tree (Nhiều biến)
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_tr_m, y_tr_m)
pred_dt = dt.predict(X_te_m)

print("1. Linear Regression (1 biến X)    - MSE:", round(mean_squared_error(y_te1, pred_lr1), 2))
print("2. Linear Regression (Nhiều biến)  - MSE:", round(mean_squared_error(y_te_m, pred_lr_multi), 2))
print("3. Decision Tree (Nhiều biến)      - MSE:", round(mean_squared_error(y_te_m, pred_dt), 2))
print("=> Nhận xét: Thêm biến không có ý nghĩa thực sự có thể không làm giảm MSE. Decision Tree trong trường hợp dữ liệu tuyến tính đơn giản này có thể bị overfitting và cho sai số (MSE) cao hơn Linear Regression.")


print("\n=== BÀI NC 2: VẼ BIỂU ĐỒ THỰC TẾ VS DỰ ĐOÁN ===")
plt.figure(figsize=(8, 5))
plt.scatter(y_te1, pred_lr1, color='blue', alpha=0.6)
# Vẽ đường tham chiếu y = x (Dự đoán hoàn hảo)
p1 = max(max(pred_lr1), max(y_te1))
p2 = min(min(pred_lr1), min(y_te1))
plt.plot([p1, p2], [p1, p2], 'r--', lw=2)
plt.xlabel("Giá trị Thực tế (Actual)")
plt.ylabel("Giá trị Dự đoán (Predicted)")
plt.title("Bài NC 2: So sánh Thực tế và Dự đoán (Linear Regression)")
plt.show()


print("\n=== BÀI NC 3: MA TRẬN TƯƠNG QUAN ===")
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
# Thêm số liệu vào ô
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = plt.text(j, i, round(corr.iloc[i, j], 2), ha="center", va="center", color="black")
plt.title("Bài NC 3: Ma trận tương quan (Correlation Matrix)")
plt.tight_layout()
plt.show()
print("=> Nhận xét: Từ ma trận nhiệt, ta thấy biến X có tương quan dương rất mạnh với Y (gần 1.0). Biến X1 và X2 có tương quan mạnh với biến phân loại Label.")


print("\n=== BÀI NC 5: CHUẨN HÓA DỮ LIỆU (LOGISTIC REGRESSION) ===")
X_cls = df[["X1", "X2"]]
y_cls = df["Label"]
X_tr_c, X_te_c, y_tr_c, y_te_c = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

# Mô hình gốc (Chưa chuẩn hóa)
model_raw = LogisticRegression(max_iter=1000)
model_raw.fit(X_tr_c, y_tr_c)
pred_raw = model_raw.predict(X_te_c)

# Mô hình đã chuẩn hóa (StandardScaler)
scaler = StandardScaler()
X_tr_scaled = scaler.fit_transform(X_tr_c)
X_te_scaled = scaler.transform(X_te_c)

model_scaled = LogisticRegression(max_iter=1000)
model_scaled.fit(X_tr_scaled, y_tr_c)
pred_scaled = model_scaled.predict(X_te_scaled)

print("Accuracy CHƯA chuẩn hóa:", accuracy_score(y_te_c, pred_raw))
print("Accuracy SAU chuẩn hóa :", accuracy_score(y_te_c, pred_scaled))
print("=> Nhận xét: Với bộ dữ liệu nhỏ và các đặc trưng có cùng thang đo (0-10), chuẩn hóa có thể không làm tăng độ chính xác ngay lập tức, nhưng đây là bước bắt buộc để giúp thuật toán hội tụ nhanh và ổn định hơn với dữ liệu thực tế lớn.")


print("\n=== BÀI NC 6: ĐÁNH GIÁ MÔ HÌNH BẰNG CONFUSION MATRIX ===")
print("Ma trận nhầm lẫn (Confusion Matrix):")
print(confusion_matrix(y_te_c, pred_scaled))
print("\nBáo cáo phân loại (Classification Report):")
print(classification_report(y_te_c, pred_scaled))
print("=> Nhận xét: Ma trận nhầm lẫn cho thấy mô hình dự đoán rất tốt. Các chỉ số Precision, Recall và F1-Score đều rất cao, tỷ lệ nhầm lẫn giữa lớp 0 và 1 cực kỳ thấp.")
print("-" * 50)
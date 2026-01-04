import pandas as pd

# 1. Đọc dữ liệu từ file CSV
df = pd.read_csv('sales_data_raw.csv')

print("=== 1. XEM TRƯỚC DỮ LIỆU ===")
print(df.head())  # Xem 5 dòng đầu để hình dung cấu trúc

print("\n=== 2. KIỂM TRA TỔNG QUAN ===")
print(df.info())  # Xem kiểu dữ liệu và số lượng dòng không null

print("\n=== 3. ĐẾM SỐ LƯỢNG GIÁ TRỊ BỊ THIẾU (NULL) ===")
print(df.isnull().sum()) # Cái này cực quan trọng để biết cột nào bị hổng

print("\n=== 4. THỐNG KÊ MÔ TẢ (TÌM LỖI LOGIC) ===")
# Hàm describe() giúp nhìn nhanh min, max, mean
print(df.describe())
print("\n=== 5. BẮT ĐẦU LÀM SẠCH (DATA CLEANING) ===")

# 1. Xử lý dữ liệu thiếu (Missing Values)
# Với cột 'PurchaseAddress': Nếu không có địa chỉ thì không giao hàng được -> Xóa luôn dòng đó.
df = df.dropna(subset=['PurchaseAddress'])

# Với cột 'Quantity': Nếu thiếu, ta tạm giả định là lấy giá trị trung bình (Mean)
# Đây là kỹ thuật "Imputation" (Nội suy) thường dùng trong Big Data
mean_val = int(df['Quantity'].mean())
df['Quantity'] = df['Quantity'].fillna(mean_val)

# 2. Xử lý lỗi Logic
# Với cột 'Price': Chuyển tất cả số âm thành số dương (Trị tuyệt đối)
df['Price'] = df['Price'].abs()

# 3. Chuẩn hóa kiểu dữ liệu (Type Casting)
# Cột OrderDate khi đọc từ CSV thường bị hiểu là String (chuỗi), cần chuyển về dạng Date để tính toán thời gian
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# 4. Tạo thêm cột mới (Feature Engineering)
# Sếp muốn biết doanh thu, nên ta cần cột 'Sales' = Số lượng * Đơn giá
df['Sales'] = df['Quantity'] * df['Price']

print("--- Đã làm sạch xong! ---")
print(df.info()) # Kiểm tra lại xem còn dòng nào bị Null không
print(df.describe()) # Kiểm tra lại xem min của Price còn bị âm không

import matplotlib.pyplot as plt

print("\n=== 6. VẼ BIỂU ĐỒ BÁO CÁO (VISUALIZATION) ===")

# Câu hỏi của Sếp: "Tháng nào bán được nhiều tiền nhất?"

# 1. Trích xuất tháng từ cột OrderDate
df['Month'] = df['OrderDate'].dt.month

# 2. Tính tổng doanh thu theo từng tháng (Group By)
# Đây là kỹ thuật cực quan trọng trong SQL và Pandas
monthly_sales = df.groupby('Month')['Sales'].sum()

print("Doanh thu theo tháng (Số liệu):")
print(monthly_sales)

# 3. Vẽ biểu đồ cột (Bar Chart)
months = range(1, 13) # Từ tháng 1 đến tháng 12

plt.figure(figsize=(10, 6)) # Tạo khung hình kích thước 10x6
plt.bar(months, monthly_sales, color='skyblue') # Vẽ cột màu xanh

plt.title('Tổng Doanh Thu Theo Tháng (Năm 2025)') # Tên biểu đồ
plt.xlabel('Tháng') # Tên trục ngang
plt.ylabel('Doanh thu (VNĐ)') # Tên trục dọc
plt.xticks(months) # Hiển thị đủ số 1-12 ở trục ngang

# Định dạng số tiền trên trục Y cho dễ nhìn (tránh số khoa học 1e8)
plt.ticklabel_format(style='plain', axis='y') 

plt.show() # Hiện biểu đồ lên!
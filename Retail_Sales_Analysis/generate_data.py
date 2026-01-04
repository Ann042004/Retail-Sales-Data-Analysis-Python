import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Cấu hình dữ liệu giả lập
num_rows = 1000  # Giả lập 1000 đơn hàng
products = ['Laptop', 'Chuột không dây', 'Bàn phím cơ', 'Màn hình 24inch', 'Tai nghe', 'USB 3.0']
cities = ['Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng', 'Cần Thơ', 'Hải Phòng']
prices = {
    'Laptop': 15000000,
    'Chuột không dây': 250000,
    'Bàn phím cơ': 800000,
    'Màn hình 24inch': 3500000,
    'Tai nghe': 500000,
    'USB 3.0': 150000
}

# 2. Hàm tạo ngày ngẫu nhiên trong năm 2025
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# 3. Tạo dữ liệu
data = []
for i in range(num_rows):
    # Chọn ngẫu nhiên sản phẩm
    product = random.choice(products)
    
    # Tạo một số lỗi ngẫu nhiên (Dữ liệu bẩn) để sau này xử lý
    # 5% cơ hội số lượng bị Null (NaN)
    if random.random() < 0.05:
        quantity = np.nan
    else:
        quantity = random.randint(1, 10)
        
    # Giá tiền (đôi khi bị nhập sai là số âm hoặc 0)
    price = prices[product]
    if random.random() < 0.02: # 2% lỗi giá
        price = -price 

    order_date = random_date(start_date, end_date)
    
    # 5% cơ hội thành phố bị để trống
    city = random.choice(cities) if random.random() > 0.05 else None 
    
    data.append([i + 1, product, quantity, price, order_date, city])

# 4. Tạo DataFrame
df = pd.DataFrame(data, columns=['OrderID', 'Product', 'Quantity', 'Price', 'OrderDate', 'PurchaseAddress'])

# 5. Xuất ra file CSV
file_name = 'sales_data_raw.csv'
df.to_csv(file_name, index=False)

print(f"Xong! Đã tạo file '{file_name}' thành công. Sẵn sàng để xử lý!")
# Retail Sales Data Analysis 📊

## 📝 Project Overview
This project analyzes a simulated dataset of retail sales records using **Python**. The goal is to perform Data Cleaning, Exploratory Data Analysis (EDA), and Visualization to derive actionable business insights, such as identifying the best-performing sales months.

## 🛠 Technologies Used
* **Language:** Python 3.x
* **Libraries:** * `Pandas`: For data manipulation and cleaning (handling missing values, type casting).
    * `Matplotlib`: For data visualization.
    * `NumPy`: For numerical operations.

## ⚙️ Key Features & Workflow
1.  **Data Generation:** created a script to simulate a realistic sales dataset (`sales_data_raw.csv`) containing 1000 records with intentional errors (null values, negative prices) to mimic real-world scenarios.
2.  **Data Cleaning (ETL):** * Handled missing values in `PurchaseAddress` and `Quantity` columns using Drop and Mean Imputation techniques.
    * Corrected logical errors (negative values in `Price` column).
    * Converted `OrderDate` to DateTime objects for time-series analysis.
3.  **Data Analysis:** calculated total sales revenue (`Price` * `Quantity`).
4.  **Visualization:** Plotted monthly sales trends to identify peak seasons.

## 💡 Key Insights
* **Best Sales Month:** The analysis revealed that **July** had the highest sales revenue.
* **Data Integrity:** Successfully cleaned and processed 94.4% of the raw data for accurate reporting.

## 🚀 How to Run
1.  Clone the repository.
2.  Run `generate_data.py` to create the dataset.
3.  Run `analysis.py` to see the cleaning process and the final sales chart.

---
*Author: [Tên của bạn]*

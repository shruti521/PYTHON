# Data Analysis on CSV Files using Pandas

# 1️⃣ Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2️⃣ Load the CSV file

df = pd.read_csv("E:\PRACTICE _TASK\DataAnalysisOnCSV\sales_data.csv")


# 3️⃣ View first few rows
print("First 5 rows of the data:")
print(df.head())

# 4️⃣ Basic info about dataset
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 5️⃣ Example groupby analysis
# Assuming your CSV has columns: 'Region', 'Product', 'Sales'
# Group sales by Region
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
print("\nTotal Sales by Region:")
print(region_sales)

# Group sales by Product
product_sales = df.groupby('Product')['Sales'].sum().reset_index()
print("\nTotal Sales by Product:")
print(product_sales)

# 6️⃣ Plot sales by Region
plt.figure(figsize=(8,5))
plt.bar(region_sales['Region'], region_sales['Sales'], color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

# 7️⃣ Plot sales by Product
plt.figure(figsize=(8,5))
plt.bar(product_sales['Product'], product_sales['Sales'], color='lightgreen')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

# 8️⃣ If you have Date column, analyze monthly sales
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    plt.figure(figsize=(10,5))
    plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Sales'], marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

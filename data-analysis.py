import pandas as pd

df = pd.read_csv("sales.csv")

# Basic analysis
total_sales = df["amount"].sum()
average_sales = df["amount"].mean()

print(f"Total Sales: {total_sales}")
print(f"Average Sale Amount: {average_sales}")

# Group by category
sales_by_category = df.groupby("category")["amount"].sum()
print(sales_by_category)

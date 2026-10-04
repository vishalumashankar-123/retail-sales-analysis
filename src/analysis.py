import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------
# Create visualization folder
# --------------------------------

os.makedirs("visualizations", exist_ok=True)


# --------------------------------
# Load dataset
# --------------------------------

df = pd.read_csv(
    "data/retail_sales.csv",
    sep=";",
    encoding="cp1252"
)

print("First 5 rows:")
print(df.head())


# --------------------------------
# Display columns
# --------------------------------

print("\nColumns:")
print(df.columns.tolist())


# --------------------------------
# Convert Date column
# --------------------------------

df["Date"] = pd.to_datetime(df["Date"])


# --------------------------------
# Monthly Sales
# --------------------------------

monthly_sales = (
    df.groupby(["Month_sort", "Month"])["Total Amount"]
    .sum()
    .reset_index()
    .sort_values("Month_sort")
)

print("\nMonthly Sales:")
print(monthly_sales)


# --------------------------------
# Category-wise Revenue
# --------------------------------

category_revenue = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Revenue:")
print(category_revenue)


# --------------------------------
# Best-Selling Category
# --------------------------------

best_category = category_revenue.idxmax()

print("\nBest-Selling Category:")
print(best_category)


# --------------------------------
# Total Sales
# --------------------------------

total_sales = df["Total Amount"].sum()

print("\nTotal Sales:")
print(total_sales)


# --------------------------------
# Total Quantity Sold
# --------------------------------

total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(total_quantity)


# --------------------------------
# Monthly Sales Chart
# --------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    monthly_sales["Month"],
    monthly_sales["Total Amount"]
)

plt.title("Monthly Sales Trend - Retail Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/monthly_sales.png")

plt.close()


# --------------------------------
# Category-wise Revenue Chart
# --------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    category_revenue.index,
    category_revenue.values
)

plt.title("Category-wise Revenue Analysis")
plt.xlabel("Product Category")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("visualizations/category_revenue.png")

plt.close()


print("\nVisualizations created successfully!")
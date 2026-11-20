# Sample data: monthly sales for four products, shown in a bar chart.

from pathlib import Path

import matplotlib.pyplot as plt

products = ["Books", "Pens", "Bags", "Notebooks"]
sales = [120, 250, 80, 170]

plt.bar(products, sales, color="steelblue")
plt.title("Retail Sales by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
chart_path = Path(__file__).with_name("retail_sales_chart.png")
plt.savefig(chart_path)
plt.show()

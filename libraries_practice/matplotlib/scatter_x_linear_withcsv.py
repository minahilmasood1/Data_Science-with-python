import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("C:/Users/my pc/Downloads/ecommerce_sales_analytics_5000.csv",
                 parse_dates=["order_date"])
#reducing the file
df = df.sample(n=100)
monthly_revenue =( df.set_index("order_date")["revenue"]
                  .resample("ME")
                  .sum()
)

plt.plot(monthly_revenue.index,monthly_revenue.values,
         linewidth=2,
         marker=1)
plt.title("Monthly_revene trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
#Scatter plot
plt.scatter(monthly_revenue.index,monthly_revenue.values,
            marker='o',
            linewidths=2,
            alpha=1,
            label="sales")
plt.title("Sales x revenue")
plt.xlabel("Sales")
plt.ylabel("revenue")
plt.show()

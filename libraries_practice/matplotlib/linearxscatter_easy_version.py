import matplotlib.pyplot as plt
sales = [250, 210, 200, 150, 149, 100, 50]
revenue = [2000,1800,1750,1200,1180,900,450]
plt.plot(sales, revenue,
                  linewidth=2,
                  alpha=0.8,
                  label="Sales")

plt.title("sales x revenue")
plt.xlabel("sales")
plt.ylabel("revenue")
plt.show()
#Scatter plot
plt.scatter(sales,revenue,
            marker='o',
            linewidths=2,
            alpha=1,
            label="sales")
plt.title("Sales x revenue")
plt.xlabel("Sales")
plt.ylabel("revenue")
plt.show()

Total_sales = 0
Average_sales = 0
for i in range(1,6):
    
    sales = int(input(f"Enter sales amount for employee {i}: "))
    Total_sales += sales
    Average_sales = Total_sales/5
    if sales < 50000:
        tax = (5 * 50000)/100
    elif 50000 <= sales <= 1000000:
        tax = (10 * 50000)/100
    elif sales > 1000000:
        tax = (15 * 50000)/100
    
    print(f"Employee {i}:\nSales Amount: {sales}\nTax Amount: {tax}")
    

print(f"Total Sales: {Total_sales}")
print(f"Average Sales: {Average_sales}")

# Q30. Write a program using matplotlib to plot line and bar graphs.
import matplotlib.pyplot as plt

# Data for plotting
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_2022 = [150, 200, 250, 300, 280, 350]
sales_2023 = [180, 210, 260, 320, 300, 380]

# --- Line Graph ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st subplot
plt.plot(months, sales_2022, marker='o', linestyle='-', color='blue', label='2022')
plt.plot(months, sales_2023, marker='s', linestyle='--', color='green', label='2023')
plt.title('Monthly Sales Trend (Line Graph)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)

# --- Bar Graph ---
plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd subplot
x_pos = range(len(months))
width = 0.35

plt.bar([x - width/2 for x in x_pos], sales_2022, width, label='2022', color='orange')
plt.bar([x + width/2 for x in x_pos], sales_2023, width, label='2023', color='purple')

plt.title('Monthly Sales Comparison (Bar Graph)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.xticks(x_pos, months)
plt.legend()

plt.tight_layout()
plt.savefig("q30_plot.png") # Save instead of pop-up to not block the script in terminal
print("Plot saved successfully as 'q30_plot.png'")
# plt.show() # Uncomment to view plot interactively

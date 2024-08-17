import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
data = pd.read_csv('../data/logistics_data_enhanced.csv')

average_efficiency_per_year = data.groupby('year')['efficiency_metric'].mean()

# Plot the average efficiency metric over time
plt.figure(figsize=(12, 6))
average_efficiency_per_year.plot(kind='line', marker='o', color='blue')
plt.title('Average Efficiency Metric Over Time')
plt.xlabel('Year')
plt.ylabel('Average Efficiency Metric')
plt.grid(True)
plt.savefig('../results/lineplot_average_efficiency_over_time.png')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
data = pd.read_csv('../data/logistics_data_enhanced.csv')


grouped_data = data.groupby(['year', 'blockchain_implementation'])['efficiency_metric'].mean().unstack()

# Plot the grouped bar chart
plt.figure(figsize=(12, 6))
grouped_data.plot(kind='bar', figsize=(12, 6))
plt.title('Average Efficiency Metric by Year and Blockchain Implementation')
plt.xlabel('Year')
plt.ylabel('Average Efficiency Metric')
plt.legend(title='Blockchain Implementation', loc='best')
plt.grid(True)
plt.savefig('../results/barchart_efficiency_blockchain_year.png')
plt.show()

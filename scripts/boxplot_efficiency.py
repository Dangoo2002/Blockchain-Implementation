import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the processed data
data = pd.read_csv('../data/logistics_data_enhanced.csv')

# Boxplot for efficiency_metric by blockchain_implementation
plt.figure(figsize=(10, 6))
sns.boxplot(x='blockchain_implementation', y='efficiency_metric', data=data)
plt.title('Efficiency Distribution by Blockchain Implementation')
plt.xlabel('Blockchain Implementation')
plt.ylabel('Efficiency Metric')
plt.savefig('../results/boxplot_efficiency_blockchain.png')
plt.show()

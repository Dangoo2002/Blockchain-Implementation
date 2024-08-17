import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_cleaned = pd.read_csv('../data/logistics_data_processed.csv')

# Calculate the correlation matrix
correlation_matrix = data_cleaned.corr()

# Plot the correlation matrix using a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Key Metrics')
plt.tight_layout()


plt.savefig('../results/correlation_matrix.png') 
plt.show()  

import pandas as pd
import matplotlib.pyplot as plt


data_cleaned = pd.read_csv('../data/logistics_data_processed.csv')

security_analysis = data_cleaned.groupby('blockchain_implementation')['security_metric'].mean()

# Plot the security metric before and after blockchain implementation
plt.figure(figsize=(10, 6))
security_analysis.plot(kind='bar', color=['red', 'blue'])
plt.title('Security Metric Before and After Blockchain')
plt.xlabel('Blockchain Implementation')
plt.ylabel('Average Security Metric')
plt.xticks(ticks=[0, 1], labels=['Before', 'After'], rotation=0)
plt.grid(axis='y')


plt.tight_layout()
plt.savefig('../results/security_metric_analysis.png')  # Save the plot
plt.show() 

import pandas as pd
import matplotlib.pyplot as plt


data_cleaned = pd.read_csv('../data/logistics_data_processed.csv')

transparency_trend = data_cleaned.groupby('year')['transparency_metric'].mean()

# Plot the transparency trend over time
plt.figure(figsize=(10, 6))
transparency_trend.plot(kind='line', marker='o', color='green')
plt.title('Transparency Metric Improvement Over Years')
plt.xlabel('Year')
plt.ylabel('Average Transparency Metric')
plt.grid(True)
plt.tight_layout()
plt.savefig('../results/lineplot_transparency_trend.png')  
plt.show() 

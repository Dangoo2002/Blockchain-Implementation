import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the enhanced data
data = pd.read_csv('../data/logistics_data_enhanced.csv')



print("Columns in the dataset:", data.columns)


X = data[['blockchain_implementation', 'shipment_volume', 'number_of_partners_involved']]  
y = data['efficiency_metric']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Plotting the Regression Line
plt.figure(figsize=(10, 6))
plt.scatter(X_test['blockchain_implementation'], y_test, color='blue')
plt.plot(X_test['blockchain_implementation'], y_pred, color='red', linewidth=2)
plt.title('Blockchain Implementation vs. Efficiency')
plt.xlabel('Blockchain Implementation')
plt.ylabel('Efficiency Metric')
plt.savefig('../results/regression_plot.png')
plt.show()

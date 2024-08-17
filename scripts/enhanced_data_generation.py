import pandas as pd
import numpy as np
import os


os.makedirs('../data', exist_ok=True)


np.random.seed(42)


data = pd.DataFrame({
    'blockchain_implementation': np.random.randint(0, 2, 100),  # Binary: 0 or 1
    'efficiency_metric': np.random.normal(100, 10, 100) + np.random.randint(0, 2, 100) * 10,
    'transparency_metric': np.random.normal(50, 5, 100) + np.random.randint(0, 2, 100) * 5,
    'security_metric': np.random.normal(75, 7, 100) + np.random.randint(0, 2, 100) * 8,
    'shipment_volume': np.random.normal(500, 50, 100),
    'average_delivery_time': np.random.normal(5, 0.5, 100),
    'number_of_partners_involved': np.random.randint(1, 10, 100),
    'year': np.random.randint(2015, 2023, 100)
})

# Save the enhanced data to CSV
data.to_csv('../data/logistics_data_enhanced.csv', index=False)
print("Enhanced logistics_data.csv has been created in the data/ directory.")

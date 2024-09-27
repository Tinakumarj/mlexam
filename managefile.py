import pandas as pd
import random

# Constants
num_rows = 150
categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']

# Generate data
data = {
    'Item_ID': [f'Item_{i + 1}' for i in range(num_rows)],
    'Item_Name': [f'Item_{i + 1}' for i in range(num_rows)],
    'Category': [random.choice(categories) for _ in range(num_rows)],
    'Stock_quantity': [random.randint(1, 100) for _ in range(num_rows)],
    'Price': [round(random.uniform(5.0, 500.0), 2) for _ in range(num_rows)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_file_path = 'inventory_data.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file '{csv_file_path}' with {num_rows} rows has been generated.")

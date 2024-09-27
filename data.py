import pandas as pd

# Load the existing dataset
df = pd.read_csv('inventory_data.csv')  # Ensure this matches your actual CSV file name

# Add a new column for Restock Recommendations
# For demonstration, we’ll add a simple restock recommendation based on stock quantity
df['Restock_Recommendation'] = df['Stock_quantity'].apply(lambda x: 'Restock' if x < 20 else 'Sufficient Stock')

# Save the modified dataset
df.to_csv('inventory_data.csv', index=False)

print("The 'Restock_Recommendation' column has been added and the dataset has been saved.")

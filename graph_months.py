import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'datasets/88.csv'  # Path to CSV file
data = pd.read_csv(file_path)

# Convert 'dttm_utc' column to datetime format for plotting
data['dttm_utc'] = pd.to_datetime(data['dttm_utc'])

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data['dttm_utc'], data['value'], label='Energy Value', color='blue')
plt.title('Energy Readings Over Time')
plt.xlabel('Time')
plt.ylabel('Energy Value')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjusts plot parameters to give some padding
plt.legend()
plt.show()
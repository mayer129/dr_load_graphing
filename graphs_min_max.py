import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the energy consumption data
file_path = 'datasets/88.csv'  # Path to CSV file
data = pd.read_csv(file_path)

# Convert 'dttm_utc' column to datetime format for plotting
data['dttm_utc'] = pd.to_datetime(data['dttm_utc'])

# Exclude entries with a value of 0 before finding the min and max
data_non_zero = data[data['value'] != 0]
min_load_index = data_non_zero['value'].idxmin()
max_load_index = data_non_zero['value'].idxmax()

min_load = data_non_zero.loc[[min_load_index]]
max_load = data_non_zero.loc[[max_load_index]]

# Plotting the entire dataset
plt.figure(figsize=(15, 7))
plt.plot(data['dttm_utc'], data['value'], label='Energy Consumption', linestyle='-', alpha=0.7)

# Highlighting the first occurrence of minimum (excluding zeros) and maximum points
plt.scatter(min_load['dttm_utc'], min_load['value'], color='red', zorder=5, label='Minimum Load (Excluding Zeros)')
plt.scatter(max_load['dttm_utc'], max_load['value'], color='green', zorder=5, label='Maximum Load')

# Annotating the first occurrence of minimum (excluding zeros) and maximum points
plt.annotate(f'Min: {min_load["value"].iloc[0]}', (min_load['dttm_utc'].iloc[0], min_load['value'].iloc[0]), textcoords="offset points", xytext=(-15,-10), ha='center', color='red')
plt.annotate(f'Max: {max_load["value"].iloc[0]}', (max_load['dttm_utc'].iloc[0], max_load['value'].iloc[0]), textcoords="offset points", xytext=(-15,10), ha='center', color='green')

plt.title('Energy Consumption Over Time with Highlighted Extremes (Excluding Zeros)')
plt.xlabel('Time')
plt.ylabel('Energy Consumption')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

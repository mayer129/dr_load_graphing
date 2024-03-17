import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the energy consumption data
file_path = 'datasets/88.csv'  # Path to CSV file
data = pd.read_csv(file_path)

# Convert 'dttm_utc' column to datetime format
data['dttm_utc'] = pd.to_datetime(data['dttm_utc'])

# Filter for July 18, 2012
data_july_18 = data[(data['dttm_utc'] >= '2012-07-18') & (data['dttm_utc'] < '2012-07-19')]

# Plotting
plt.figure(figsize=(30, 7))
plt.plot(data_july_18['dttm_utc'], data_july_18['value'], label='Energy Consumption', marker='o', linestyle='-')

# Formatting the x-axis to show time in 10-minute intervals
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.title('Energy Consumption on July 18, 2012')
plt.xlabel('Time')
plt.ylabel('Energy Consumption')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

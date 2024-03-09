import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file
file_path = 'datasets/88.csv'  # Path to CSV file
data = pd.read_csv(file_path)

# Convert 'dttm_utc' column to datetime format
data['dttm_utc'] = pd.to_datetime(data['dttm_utc'])

# Filter data for the second week of January 2012
data_second_week_january = data[(data['dttm_utc'] >= '2012-01-22') & (data['dttm_utc'] <= '2012-01-29')]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data_second_week_january['dttm_utc'], data_second_week_january['value'], label='Energy Value', color='blue')

# Formatting the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a %b %d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.title('Energy Readings for the Fourth Week of January 2012')
plt.xlabel('Time')
plt.ylabel('Energy Value')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjusts plot parameters to give some padding
plt.legend()
plt.show()

import pandas as pd

# Assuming you have a DataFrame df with columns 'Date', 'Time', 'Volume'
# and other relevant columns like 'Open', 'High', 'Low', 'Close'
# Make sure 'Date' and 'Time' are combined into a datetime column

# Sample data creation (replace this with your actual data loading)
data = {'Date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-01', '2024-01-01'],
        'Time': ['09:15:00', '09:16:00', '09:17:00', '09:18:00', '09:19:00'],
        'Volume': [1000, 1200, 800, 1500, 2000]}
df = pd.DataFrame(data)
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Function to calculate rank based on volume for last 5 days at a specific time
def calculate_rank(df, datetime_col, volume_col):
    # Get the unique times in the DataFrame
    unique_times = df[datetime_col].dt.time.unique()
    ranks = []
    for time in unique_times:
        # Filter the DataFrame for the specific time
        mask = df[datetime_col].dt.time == time
        subset = df[mask]
        # Get the last 5 days' data
        last_5_days = subset.iloc[-5:]
        # Rank the volume in descending order
        ranks.extend(last_5_days[volume_col].rank(method='max', ascending=False))
    return ranks

# Calculate ranks and add them to the DataFrame as a new column
df['Rank'] = calculate_rank(df, 'DateTime', 'Volume')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV
df = pd.read_csv('Opened_Cases_RR_AllTime.csv',   # file to read
                 parse_dates=['Opened Date'],  # columns to parse as dates
                 usecols=['Opened Date'])

# Sort them by date
df.sort_values(by=['Opened Date'], inplace=True, ascending=True)
# Convert the Opened Date to a Day of Week
df['Day of Week'] = df['Opened Date'].dt.dayofweek
df = df[df['Day of Week'] <= 4]

# Create the # of Cases column from the Opened Date
df['# of Cases'] = df.groupby('Opened Date')['Opened Date'].transform('count')

# Now that we have our # of Cases counted up by day, let's drop the non-unique days
df.drop_duplicates('Opened Date', inplace=True)

# Let's see what it looks like and plot it
df.plot(x='Opened Date', y='# of Cases', figsize=(48, 8))
# Save it
plt.savefig('output.png')

# Save the new CSV
df.to_csv('Opened_Cases_RR_AllTime_Modified.csv', encoding='utf-8', index=False)

# Random debugging shit
pd.option_context('display.max_rows', None, 'display.max_columns', None)
print(df)

# Gotta show it in the IDE!
plt.show()

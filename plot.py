import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV
df = pd.read_csv('Opened_Cases_RR_AllTime.csv')

# Drop unnecessary columns
df.drop(['Case Number', 'Issue Summary', 'Account Name'], axis=1,
        inplace=True)

# Convert the Opened Date column to datetime
df['Opened Date'] = pd.to_datetime(df['Opened Date'])

# Sort them by date
df.sort_values(by=['Opened Date'], inplace=True, ascending=True)
# Convert the Opened Date to a Day of Week
# df['Day of Week'] = df.loc(df['Opened Date'].dt.dayofweek <= 4)
df['Day of Week'] = df['Opened Date'].dt.dayofweek

# Create the # of Cases column from the Opened Date
df['# of Cases'] = df.groupby('Opened Date')['Opened Date'].transform('count')

# Now that we have our # of Cases counted up by day, let's drop the non-unique days
df.drop_duplicates('Opened Date', inplace=True)

# Let's see what it looks like and plot it
df.plot(x='Opened Date', y='# of Cases')

# Gotta show it in the IDE!
plt.show()
# Save it
plt.savefig('output.png')

pd.set_option('display.max_rows', None)
print(df)
print(max(df["# of Cases"]))

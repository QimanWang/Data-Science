
# we will be analyzing some 911 call data from
# [Kaggle](https://www.kaggle.com/mchirico/montcoalert).
# The data contains the following fields:
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('911.csv')

df.info()
df.head()

df['zip'].value_counts().head(5)
# top 5 zipcodes with most calls

df['twp'].value_counts().head(5)
# top 5 townships with most calls

df['title'].nunique()
# how many unique call titles are there

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
# create a new column called Reason

df['Reason'].value_counts()
# most common call Reason

sns.countplot(x='Reason', data=df, palette='viridis')
# plot the call Reason
# EMS ranks number 1

type(df['timeStamp'].iloc[0])
# the time is stored as str type
# so we need to conver it to integer

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# convert string to Datetime object format

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
# created 3 new columns  hours, month, day of week

dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
# convert integer to correspond week days as string

sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plot call volumn of every day of the week,
# seperated the 3 reason into 3 color

sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plot every month and the call volume

# since we are mdata for a few month,
# we can "fill in the best estimae data"
byMonth = df.groupby('Month').count()
byMonth['twp'].plot()

sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
# plot of the estimated volume

df['Date'] = df['timeStamp'].apply(lambda t: t.date())
# create a new Date column that contain the date

df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
# plot everyday onto a line plot
# we see that February have the highest peak
# May have the lowest peak

df[df['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
# plot by traffic, Febraury have the highest call vloume

df[df['Reason'] == 'Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
# plot by Fire, several month have high call volumne aboout Fire

df[df['Reason'] == 'EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
# plot by EMS, every month have about the same call volume
# May have the lowest peak

dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
# group by row: date , col:hour

plt.figure(figsize=(12, 6))
sns.heatmap(dayHour, cmap='viridis')
# Plot heatmap, 9am - 6pm havet he highest call volume

sns.clustermap(dayHour, cmap='viridis')
# cluster map

dayMonth = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()
# we group row: day of week , col: Month

plt.figure(figsize=(12, 6))
sns.heatmap(dayMonth, cmap='viridis')
# August and december have the lowest call volume

sns.clustermap(dayMonth, cmap='viridis')
# cluster map

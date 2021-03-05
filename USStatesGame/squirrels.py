import pandas

df = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
df = df.value_counts(['Primary Fur Color'])
df.to_csv('squirrels.csv')
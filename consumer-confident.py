consumer_confidence = pd.read_csv("consumerconfus.csv")
consumer_confidence['TIME'] = pd.to_datetime(consumer_confidence.TIME)
del consumer_confidence['MEASURE']
del consumer_confidence['Flag Codes']
del consumer_confidence['SUBJECT']

print(consumer_confidence['LOCATION'].unique())

USA = consumer_confidence[consumer_confidence['LOCATION']=='USA']
change_2015 = USA[USA['TIME'].dt.year == 2015]
change_2015 = change_2015.groupby(change_2015.TIME.dt.month).mean()

change_2016 = USA[USA['TIME'].dt.year == 2016]
change_2016 = change_2016.groupby(change_2016.TIME.dt.month).mean()

change_2017 = USA[USA['TIME'].dt.year == 2017]
change_2017 = change_2017.groupby(change_2017.TIME.dt.month).mean()

EA19 = consumer_confidence[consumer_confidence['LOCATION']=='EA19']
change_2015_EU = EA19[EA19['TIME'].dt.year == 2015]
change_2015_EU = change_2015_EU.groupby(change_2015_EU.TIME.dt.month).mean()

change_2016_EU = EA19[EA19['TIME'].dt.year == 2016]
change_2016_EU = change_2016_EU.groupby(change_2016_EU.TIME.dt.month).mean()

change_2017_EU = EA19[EA19['TIME'].dt.year == 2017]
change_2017_EU = change_2017_EU.groupby(change_2017_EU.TIME.dt.month).mean()

print(change_2015.pct_change().max()*100)
print(change_2016.pct_change().max()*100)
print(change_2017.pct_change().max()*100)

print(change_2015_EU.pct_change().max()*100)
print(change_2016_EU.pct_change().max()*100)
print(change_2017_EU.pct_change().max()*100)


import pandas as pd


# read table data
MasterDataframe = pd.read_csv('data.csv')

# calculate the total price of the transactione
totalPercent = MasterDataframe['total'].sum()
MasterDataframe['date'] = pd.to_datetime(MasterDataframe['date']) - pd.to_timedelta(7, unit='d')
MasterDataframe['totalPercent']=  MasterDataframe['total'].apply(lambda x: x*100/totalPercent)

#create month to split data
MasterDataframe['YearMonth'] = pd.to_datetime(MasterDataframe['date']).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))

#get total price for each article for week
itemReport = MasterDataframe.where(MasterDataframe["YearMonth"]
 < "2018-4").groupby(['article', pd.Grouper(key='date',
  freq='W-MON')])['total'].sum()

# get top 10 article
article = MasterDataframe.where(MasterDataframe["YearMonth"] < "2018-4").groupby('article')['total'].sum().sort_values(ascending=False).head(10)
articleList = (list(article.keys()))

# get list item whose the frequency reach 5/6 weeek
itemReport =itemReport.groupby(['article']).count() > 5
itemReport=itemReport.loc[itemReport.values==True]


# get item whith has both high revenue and  frequency
final_item = []
itemList = (list(itemReport.keys()))
for item in itemList:
    if item in articleList:
        final_item.append(item)

print(final_item)
print(len(final_item))

# save popular item to csv
result = MasterDataframe.where(MasterDataframe["article"]
    .isin(final_item)).where(MasterDataframe["YearMonth"] 
    < "2018-4").groupby('article').agg(
    {'total': ['sum'],'csn':lambda x: x.nunique()})

result.to_csv("res1.csv")


# get item whith has high unique consumer bought
result = MasterDataframe.where(MasterDataframe["YearMonth"] 
    < "2018-4").groupby('article').agg(
    {'csn':lambda x: x.nunique()}).sort_values('csn',ascending=False).head(10)
final_list = list(result.iloc[:, 0].keys())


# save popular item to csv
result = MasterDataframe.where(MasterDataframe["article"]
    .isin(final_list)).where(MasterDataframe["YearMonth"] 
    < "2018-4").groupby('article').agg(
    {'total': ['sum'],'csn':lambda x: x.nunique()})

result.to_csv("res2.csv")

# the graph will be export from the CSV from excel!
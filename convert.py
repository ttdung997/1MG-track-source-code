import pandas as pd
import json

# open data csv file
MasterDataframe = pd.read_csv('VinIDRecruitChallenge_MLTrack_DataSet.csv')

# create empty list
csnList = []
dateList = []
articleList = []
salesquantityList = []
priceList = []
itemList = []
totalList = []

# Function to convert list to string  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 = str1 + ", " + ele  
    
    # return string  
    return str1 


# read row in dataframe
for index, row in MasterDataframe.iterrows():
    jsonData = json.loads(row["transaction_info"].replace("'",'"'))
    item = []
    #parse json
    for line in jsonData:
        csnList.append(row["csn"])
        dateList.append(row["date"])
        articleList.append(line["article"])
        salesquantityList.append(line["salesquantity"])
        priceList.append(line["price"])
        totalList.append(float(line["salesquantity"])*float(line["price"]))
        if line["article"] not in item:
            item.append(line["article"])
    itemList.append(item)


# save data to dictionary
final = {
    'csn': csnList,
    'date': dateList,
    'article': articleList,
    'salesquantity': salesquantityList,
    'price': priceList,
    'total': totalList
}

# convert data to the traditional table for statistic
df = pd.DataFrame (final, columns = ['csn','date','article','salesquantity','price','total'])
df.to_csv("data.csv")



# save item data to csv for apriori algorithm
textfile = open("output.txt", "w")
for element in itemList:
    myStr = listToString(element)
    textfile.write(myStr + "\n")
textfile.close()



from efficient_apriori import apriori

import pandas as pd

# load item data
transactions = []
data = [line.rstrip('\n') for line in open('item.csv')]

for line in data:
    line= line.split(",")
    transactions.append(tuple(line))

# set  min_support, min_confidence parameter to apriori
itemsets, rules = apriori(transactions, min_support=0.005,  min_confidence=0.01)




# ger output rule
for rule in sorted(rules, key=lambda rule: rule.lift):
    print(rule)
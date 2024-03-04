import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from google.colab import drive

# Mounting Google Drive
drive.mount('/content/drive')

# Loading the Data
data = pd.read_excel('/content/drive/My Drive/X/CleanData_Fix.xlsx')

# Dropping the rows without any invoice number
data.dropna(axis=0, subset=['transactionID'], inplace=True)
data['transactionID'] = data['transactionID'].astype('str')

# Creating the basket dataset
basket = (data.groupby(['transactionID', 'ProductName'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('transactionID'))

# Defining the hot encoding function to make the data suitable for the concerned libraries
def hot_encode(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

# Encoding the datasets
basket_encoded = basket.applymap(hot_encode)
basket = basket_encoded.astype(bool)

# Building the model
frequent_itemsets = apriori(basket, min_support=0.002, use_colnames=True)

# Collecting the inferred rules with confidence metric
rules_confidence = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.08)

# Filtering the rules based on lift metric
rules_filtered = rules_confidence[rules_confidence['lift'] >= 1]

rules = rules_filtered

#this for june, make for july as well
data_june = pd.read_excel('/content/drive/My Drive/X/june.xlsx')
item_counts_june = data_june.groupby('ProductName')['Quantity'].sum()

less_popular_items_june = item_counts_june[(item_counts_june == 1) | (item_counts_june == 0)].index.tolist()

print("Item 0 or 1:")
print(len(less_popular_items_june))
for item in less_popular_items_june:
    print(item)

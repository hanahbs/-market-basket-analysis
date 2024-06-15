# Market Basket Analysis
Aim: Identify associations between products for bundle recommendations and enhance cross-selling strategies

## Problem of the store
=> How can we increase sales for a product that isn't selling well?

### Important Notes
Tools and Materials:
+ 2 months data of the store including Transaction ID, Product Name, Quantity, Category of the Item in June and July
+ python language
+ google colab IDE
  
## Identify the less popular product  
=> we found in June there are 3,111 items were bought either 0 or once, and in July, 2,922 items were bought either 0 or once

## Find the Association Rules
find the association rules which mean identifying products that tend to be bought together.

=> we found there are 10 rules, which is:
![image](https://github.com/hanahbs/market-basket-analysis/assets/98167908/65926d6f-c733-4dff-a795-25a06b5a4f44)

## FINALLY!!
=> there 2 ways for bundles,
1) Replace a product from one of the association rule products with a less popular product, provided that they belong to the same category.
![image](https://github.com/hanahbs/market-basket-analysis/assets/98167908/e58ebd4c-6dcc-4870-bd56-26daee9b7839)


3) Create a bundle pairing association rules with less popular products.
We can combine them based on previous transactions, specifically, make bundles from products that have been purchased together through association rules with the less popular product. We've identified 21 instances of such associations.
![image](https://github.com/hanahbs/market-basket-analysis/assets/98167908/7ec04f2c-72cf-48cb-8fa5-31ba511a352c)

## Evaluation
=> The store received it with appreciation, and they mentioned that it is a good strategy to boost the sales of their products that isn't selling well

### test


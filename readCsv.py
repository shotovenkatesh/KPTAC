import pandas as pd

df = pd.read_csv("menu.csv")
df['Name'] = df['Name'].str.title()
df['Description'] = df['Description'].str.title()

data_dict = df.to_dict('records')

#the name from csv should match here
names = [item['Name'] for item in data_dict]
price = [item['Price'] for item in data_dict]
# category = [item['Category'] for item in data_dict]
description = [item['Description'] for item in data_dict]
# print(names)
# print(price)
# print(category)
# def fetch_from_csv():
#     if len(names) == len(price) == len(category):
#         return (names,price,category)
#     else:
#         return "The length does not match, make sure the datat is correct"

def get_names():
    return names

def get_prices():
    return price
#
# def get_c():
#     return category

def get_des():
    return description

print(get_names())
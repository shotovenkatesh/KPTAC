import pandas as pd

df = pd.read_csv("karaf.csv")
df['Category'] = df['Category'].str.title()

data_dict = df.to_dict('records')


cat = [item['Category'] for item in data_dict]
sort_nos = [item['Sort'] for item in data_dict]
parent_cat = [item['Parent'] for item in data_dict]


def get_c():
    return cat

def get_sort():
    return sort_nos

def get_p():
    return parent_cat

# print(cat)
# print(sort_nos)
# print(parent_cat)
# import pandas as pd
#
# df = pd.read_csv("ird.csv")
# df['Name'] = df['Name'].str.title()
# # df['Description'] = df['Description'].str.title()
# # df['Category'] = df['Category'].str.title()
# # df['Price'] = df['Price'].astype(float)
#
# data_dict = df.to_dict('records')
#
# #the name from csv should match here
# names = [item['Name'] for item in data_dict]
# # des = [item['Description'] for item in data_dict]
# # cat = [item['Category'] for item in data_dict]
# # prices = [item['Price'] for item in data_dict]
# a_names = [item['Aname'] for item in data_dict]
# a_des = [item['AD'] for item in data_dict]
#
#
#
#
#
#
#
#
# # # Convert the DataFrame to a list of dictionaries
# # data_list = df.to_dict('records')
# #
# # # Print the list
# # for item in data_list:
# #     print(item)
#
#
#
#
# def get_names():
#     return names
#
# def get_anames():
#     return a_names
#
# def get_ades():
#     return a_des
#
# # def get_c():
# #     return cat
# #
# # def get_des():
# #     return des
#
# # def get_price():
# #     return prices
#
# print(names)
# print(a_names)
# print(a_des)
# # print(prices)
# # print(cat)
# # print(des)
# # print(type(des[0]))

import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
file_path = 'tara.xlsx'

# Replace 'Sheet1' with the name of the sheet in your Excel file
sheet_name = 'Sheet1'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Transform the data
df['Name'] = df['name']
df['AName'] = df['aname']
df["AD"] = df["adescription"]

names = df['Name'].tolist()
names = [name.title() for name in names]
# des= df['Description'].tolist()
# des = [str(data) for data in des]
a_names = df['AName'].tolist()
a_d = df['AD'].tolist()

def get_names():
    return names

def get_anames():
    return a_names

def get_ades():
    return a_d


# print(names[0])
# print(a_names[0])
# print(a_d[0])
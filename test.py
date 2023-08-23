import readCsv

index = 0
name = readCsv.get_names()
price = readCsv.get_prices()
category = readCsv.get_c()

last_element = len(name)

while index < last_element:
    food = name[index]
    food_price = price[index]
    food_c = category[index]
    print(food, food_price, food_c)
    index += 1

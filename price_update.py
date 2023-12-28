import time
import readCsv
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
# time.sleep(2)
#
# # signing in
# email_field = driver.find_element(By.NAME, "login").send_keys("sisis@emenu.ae")
# password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
# driver.find_element(By.NAME, "submit").click()
# time.sleep(3)
#
#
#
#
# # products drop down
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
# time.sleep(3)


index = 0
names = readCsv.get_names()
p1= readCsv.get_p1s()
p2 = readCsv.get_prices()

if len(p1) != len(p2):
    print("Lists have different lengths")
else:
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            print(f"{names[i]}  from price: {p1[i]} to {p2[i]} ")




# last_element = len(name_from_csv)
#
# while index < last_element:
#     food = name_from_csv[index]
#
#     food_d = desc_from_csv[index]
#     # print(food,food_d ,index)
#
#     # # search and find the product
#     driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').send_keys(food)
#     time.sleep(3)
#     # driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').click()
#
#     try:
#         # Find the <tr> element with class "odd"
#         odd_row = driver.find_element(By.CLASS_NAME, 'odd')
#
#         # Find the <td> element with class "td-actions text-right" within the <tr> element
#         td_element = odd_row.find_element(By.CLASS_NAME, 'td-actions.text-right')
#
#         # Find the button with class "btn btn-success" within the <td> element
#         button = td_element.find_element(By.CLASS_NAME, 'btn.btn-success')
#
#         # Click the button
#         button.click()
#
#         # You can add more actions after clicking the button if needed
#     except:
#         print(f"{food} is not in the list")
#         driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').clear()
#         index += 1
#         time.sleep(1)
#
#     else:
#         # Close the WebDriver
#         # Description column
#         ##start here
#         driver.find_element(By.XPATH,
#                             '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[2]/textarea').click()
#         time.sleep(1)
#         driver.find_element(By.TAG_NAME, 'textarea').send_keys(food_d)
#         time.sleep(3)
#
#         # this is to middle intend
#         middle_indent = driver.find_element(By.XPATH,
#                                             '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[3]/div/div/div/span[1]/span[2]/span[5]/span[3]/a[8]/span[1]').click()
#         time.sleep(1)
#         ActionChains(driver).send_keys(food_d).perform()
#         time.sleep(2)
#         ##end here
#
#         # clicking on price then sending keys
#
#         # driver.find_element(By.XPATH,
#         #                     '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[3]/ul/li[1]/a').click()
#         driver.execute_script('scrollBy(0,500)')
#
#         submit = driver.find_element(By.NAME, 'submit').click()
#         index += 1
#         time.sleep(3)
import time
from selenium.webdriver import ActionChains
import readCsv
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("alfarah-auh@emenu.ae")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
driver.find_element(By.NAME, "submit").click()

# clciking on edit pen link
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/h4').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/a/i').click()
time.sleep(2)


# products drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
time.sleep(2)

# Getting data from csv
index = 0
name_from_csv = readCsv.get_names()
price_from_csv = readCsv.get_price()
category_from_csv = readCsv.get_c()
# desc_from_csv = readCsv.get_des()

last_element = len(name_from_csv)

while index < last_element:
    food = name_from_csv[index]
    food_price = price_from_csv[index]
    food_c = category_from_csv[index]
    # food_d = desc_from_csv[index]


    # # Creating a new product
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/a').click()
    time.sleep(1)

    # clicking on name field before sending in the keys
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[1]/input').click()

    name_from_site = driver.find_element(By.NAME, "name").send_keys(food)
    # time.sleep(2)
    driver.execute_script('scrollBy(0,120)')
    # time.sleep(3)

    # Description column
    ##start here
    # driver.find_element(By.XPATH,
    #                     '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[2]/textarea').click()
    # time.sleep(1)
    # if food_d == "nannan" or food_d == "nan" or food_d == "":
    #     driver.find_element(By.TAG_NAME, 'textarea').send_keys("  ")
    # else:
    #     driver.find_element(By.TAG_NAME, 'textarea').send_keys(food_d)
    # driver.find_element(By.TAG_NAME, 'textarea').send_keys(food_d)
    # time.sleep(3)
    #
    # # this is to middle intend
    # middle_indent = driver.find_element(By.XPATH,
    #                                     '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[3]/div/div/div/span[1]/span[2]/span[5]/span[3]/a[8]/span[1]').click()
    # time.sleep(1)
    # ActionChains(driver).send_keys(food_d).perform()
    # time.sleep(2)
    ##end here

    # clicking on price then sending keys
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[2]/div/div/input[1]').click()
    # time.sleep(2)
    price_from_site = driver.find_element(By.NAME, "price_0").send_keys(food_price)
    driver.execute_script('scrollBy(0,50)')

    # this is  to locate the category field
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/button/div[1]/div/div').click()
    # time.sleep(1)
    # this is to search in the category field
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[2]/input').send_keys(
        food_c)
    # time.sleep(1)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[3]/ul/li[1]/a').click()
    driver.execute_script('scrollBy(0,500)')

    submit = driver.find_element(By.NAME, 'submit').click()
    print(f"{food} has been added")
    index += 1
    time.sleep(1)

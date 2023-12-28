import time
from selenium.webdriver import ActionChains
import read_c
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("ustunturkmen84@gmail.com")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)



# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/h4').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/a/i').click()
# time.sleep(2)




# categories drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[5]/a').click()
time.sleep(1)


# Getting data from csv
index = 0

category_from_csv = read_c.get_c()
sorts_from_csv = read_c.get_sort()
parent_from_csv = read_c.get_p()

last_element = len(category_from_csv)

while index < last_element:

    food_c = category_from_csv[index]
    sort_no = sorts_from_csv[index]
    parent_category = parent_from_csv[index]


    # # Creating a category
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/a').click()
    time.sleep(1)

    # clicking on name field before sending in the keys
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[1]/input').click()

    name_from_site = driver.find_element(By.NAME, "name").send_keys(food_c)
    time.sleep(1)


    #parent category
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[3]/div/button/div[1]/div/div').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[3]/div/div/div[2]/input').send_keys(parent_category)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[3]/div/div/div[3]/ul/li/a/span[2]').click()

    driver.execute_script('scrollBy(0,520)')

    #adding sort no
    driver.find_element(By.NAME, "sort_order").click()
    driver.find_element(By.NAME, "sort_order").send_keys(sort_no)


    # driver.execute_script('scrollBy(0,500)')

    submit = driver.find_element(By.NAME, 'submit').click()
    print(f"{food_c} has been added")
    index += 1
    time.sleep(2)

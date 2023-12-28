import time
from selenium.webdriver import ActionChains
import readCsv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("darkdooruae@gmail.com")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
driver.find_element(By.NAME, "submit").click()
time.sleep(3)

#clciking on edit pen link
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/a/i').click()
time.sleep(2)


# products drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
time.sleep(3)



index = 0
name_from_csv = readCsv.get_names()
price_from_csv = readCsv.get_prices()

last_element = len(name_from_csv)

while index < last_element:
    food = name_from_csv[index]

    food_d = price_from_csv[index]
    # print(food,food_d ,index)

    # # search and find the product
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').send_keys(food)
    time.sleep(3)
    # driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').click()

    try:
        # Find the <tr> element with class "odd"
        odd_row = driver.find_element(By.CLASS_NAME, 'odd')

        # Find the <td> element with class "td-actions text-right" within the <tr> element
        td_element = odd_row.find_element(By.CLASS_NAME, 'td-actions.text-right')

        # Find the button with class "btn btn-success" within the <td> element
        button = td_element.find_element(By.CLASS_NAME, 'btn.btn-success')

        # Click the button
        button.click()

        # You can add more actions after clicking the button if needed
    except:
        print(f"{food} is not in the list")
        driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').clear()
        index += 1
        time.sleep(1)

    else:

        ##end here

        # clicking on price then sending keys
        driver.find_element(By.NAME,'price_0').clear()
        driver.find_element(By.NAME,'price_0').send_keys(food_d)

        # driver.find_element(By.XPATH,
        #                     '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[3]/ul/li[1]/a').click()
        driver.execute_script('scrollBy(0,500)')

        submit = driver.find_element(By.NAME, 'submit').click()
        index += 1
        time.sleep(3)





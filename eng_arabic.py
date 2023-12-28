import time

from selenium.webdriver import ActionChains, Keys

import a_read_csv
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

names = a_read_csv.get_names()
a_names = a_read_csv.get_anames()
a_d = a_read_csv.get_ades()

index = 0
# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("Tara@emenu.ae")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2024")
driver.find_element(By.NAME, "submit").click()
time.sleep(1)


#clicking in on the outlet
# driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[4]/div/div[2]/h4').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[4]/div/div[2]/div[1]/a/i').click()
# time.sleep(1)



# products drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
time.sleep(2)


for _ in names:
    driver.find_element(By.XPATH,
                        '/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').send_keys(
        names[index])
    time.sleep(2)
    odd_row = driver.find_element(By.CLASS_NAME, 'odd')

    # Find the <td> element with class "td-actions text-right" within the <tr> element
    td_element = odd_row.find_element(By.CLASS_NAME, 'td-actions.text-right')

    # Find the button with class "btn btn-success" within the <td> element
    button = td_element.find_element(By.CLASS_NAME, 'btn.btn-success')

    # Click the button
    button.click()

    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul/li[1]/form/label/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/nav/div/div[2]/ul/li[1]/form/label/div/div/div[2]/ul/li[2]/a').click()
    time.sleep(1)
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(a_names[index])
    time.sleep(2)

    small_d = driver.find_element(By.NAME,"small_description")
    small_d.clear()

    driver.find_element(By.NAME, "description").clear()
    driver.find_element(By.NAME, "description").send_keys(a_d)

    # arabic to eng

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div[2]/ul/li[1]/form/label/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '/html/body/div/div[2]/nav/div/div[2]/ul/li[1]/form/label/div/div/div[2]/ul/li[1]/a').click()

    time.sleep(2)

    index += 1


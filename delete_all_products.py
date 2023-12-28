import time
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("tmeric@onedoner.com")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
driver.find_element(By.NAME, "submit").click()
time.sleep(1)


# clciking on edit pen link
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[1]/div/div[2]/h4').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/a/i').click()
time.sleep(2)

# products drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
time.sleep(2)


while True:
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[6]/a[3]/i').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[2]/form/button').click()
    time.sleep(1)


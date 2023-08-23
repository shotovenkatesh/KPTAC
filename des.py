import time
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By


DATA = ["egg bacon slider ","turkish simmit egg","turkish egg","shakshuka sandwich","shakshuka","peanut butter toast with straberry jam","truffle egg slider","haloumi with beetroot toast","egg croissant with bacon and spinach ","egg croisant poached egg with spinach","egg croissant scrambled egg ","egg benedict","classic french toast","avocado toast with egg scrambled","avocado toast with poached egg "]

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("chrizmedrano16@gmail.com")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
driver.find_element(By.NAME, "submit").click()
time.sleep(3)

# products drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
time.sleep(3)

for name in DATA:
# # Creating a new product
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/a').click()
    time.sleep(2)




    # clicking on name field before sending in the keys
    driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[1]/input').click()

    name_from_site = driver.find_element(By.NAME, "name").send_keys(name.title())
    time.sleep(2)
    driver.execute_script('scrollBy(0,120)')
    time.sleep(3)

    # #Description column
    # ##start here
    # test = "This is filled now"
    # driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[2]/textarea').click()
    # time.sleep(1)
    # driver.find_element(By.TAG_NAME,'textarea').send_keys(test)
    # time.sleep(3)
    #
    # #this is to middle intend
    # middle_indent = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[3]/div/div/div/span[1]/span[2]/span[5]/span[3]/a[8]/span[1]').click()
    # time.sleep(1)
    # ActionChains(driver).send_keys(f'{test}').perform()
    # time.sleep(2)
    # ##end here



    # clicking on price then sending keys
    driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[2]/div/div/input[1]').click()
    time.sleep(2)
    price_from_site = driver.find_element(By.NAME, "price_0").send_keys(0)
    driver.execute_script('scrollBy(0,50)')

        # this is  to locate the category field
    driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/button/div[1]/div/div').click()
    time.sleep(2)
        # this is to search in the category field
    driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[2]/input').send_keys(
            "BreakFast")
    time.sleep(1)
    driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[3]/ul/li[1]/a').click()
    driver.execute_script('scrollBy(0,500)')

    submit = driver.find_element(By.NAME, 'submit').click()
    time.sleep(4)
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

i = 0
while i >= 0:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://45ysidyz49o.typeform.com/TestAmbassdor?typeform-source=www.huawei.com")
    driver.maximize_window()
    nepal = driver.find_elements("xpath",
                                 "//div[contains(@class,'Root-sc-__sc-164255h-0 kIkYlk ChoiceRoot-sc-__sc-1g50zb3-5 ixDWjX')][.//div[contains(text(),'Jeziel')]]")
    egypt = driver.find_elements("xpath",
                                 "//div[contains(@class,'Root-sc-__sc-164255h-0 kIkYlk ChoiceRoot-sc-__sc-1g50zb3-5 ixDWjX')][.//div[contains(text(),'Egypt')]]")
    kenya = driver.find_elements("xpath",
                                 "//div[contains(@class,'Root-sc-__sc-164255h-0 kIkYlk ChoiceRoot-sc-__sc-1g50zb3-5 ixDWjX')][.//div[contains(text(),'Kenya')]]")
    button = driver.find_elements("xpath", "//button[contains(@class, 'ButtonWrapper-sc-__sc-1qu8p4z-0 iPnBIj')]")

    for picks in nepal:
        picks.click()
        break
    for picks in egypt:
        picks.click()
        break
    for picks in kenya:
        picks.click()
        break
    for picks in button:
        picks.click()
        break
    time.sleep(3)
    i = i +1
    print('Loop: ', i)
    driver.close()